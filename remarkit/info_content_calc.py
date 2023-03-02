from Bio import AlignIO
from Bio import Phylo
import itertools
import scipy
from tqdm import tqdm


def calculate_desirabilities(
        identifiers: list,
        treeness_over_rcv: list,
        saturation: list,
        treeness: list
) -> list:
    treeness_over_rcv_desirabilities = [round(((i - min(treeness_over_rcv))/(max(treeness_over_rcv) - min(treeness_over_rcv))), 6) for i in treeness_over_rcv]
    saturation_desirabilities = [round(((i - min(saturation))/(max(saturation) - min(saturation))), 6) for i in saturation]
    treeness_desirabilities = [round(((i - min(treeness))/(max(treeness) - min(treeness))), 6) for i in treeness]

    overall_desirability = []
    for tor, sat, tre in zip(treeness_over_rcv_desirabilities, saturation_desirabilities, treeness_desirabilities):
        # Weights (average permutation importance values for testing data)
        # treeness: 0.011526795
        # saturation: 0.018250758
        # tor: 0.041253792
        overall_desirability.append(sum([tor*0.041253792, sat*0.018250758, tre*0.011526795])/3)
    
    # rescale between 0 and 1
    overall_desirability = [(i - min(overall_desirability)) / (max(overall_desirability) - min(overall_desirability)) for i in overall_desirability]

    merged_df = [[a, b, c, d, e, f, g, h] for a, b, c, d, e, f, g, h in zip(identifiers, overall_desirability, treeness_over_rcv_desirabilities, saturation_desirabilities, treeness_desirabilities, treeness_over_rcv, saturation, treeness)]
    merged_df.sort(key = lambda x: x[1], reverse=True)

    return merged_df

def create_info_content_matrices(input_contents: list):
    """
    create matrices with information content
    """
    identifiers = []
    treeness_over_rcv = []
    saturation = []
    treeness = []

    for content in tqdm(input_contents):
        identifiers.append(content[0])
        info_content = calculate_information_content(content)
        treeness_over_rcv.append(info_content[0])
        saturation.append(info_content[1])
        treeness.append(info_content[2])

    return identifiers, treeness_over_rcv, saturation, treeness

def calculate_information_content(row: list):
    """
    calculate information content including treeness / rcv, saturation, treeness
    """
    alignment = AlignIO.read(open(row[1]), "fasta")
    tree = Phylo.read(row[2], "newick")

    rcv = calc_rcv(alignment)
    treeness = calc_treeness(tree)

    treeness_over_rcv = round(treeness/rcv,4)

    saturation = calc_saturation(alignment, tree)

    return [treeness_over_rcv, saturation, treeness]

    
def calc_treeness(tree):
    """
    calculate treeness
    """
    inter_len = float(0.0)
    # determine internal branch lengths
    for interal in tree.get_nonterminals():
        # only include if a branch length value is present
        if interal.branch_length != None:
            inter_len += interal.branch_length
    # determine total branch length
    total_len = tree.total_branch_length()

    return round(float(inter_len / total_len), 4)

def calc_rcv(alignment):
    """
    calculate rcv
    """
    aln_len = alignment.get_alignment_length()

    # string to hold all sequences
    concat_seq = ''
    # initialize a counter for the number of sequences in the input fasta file
    num_records = 0

    # for each record join concatSeq string and sequence as well as keeping track 
    # of the number of records
    for record in alignment:
        concat_seq  += record.seq
        num_records += 1

    # dictionary to hold the average occurence of each sequence letter
    average_d = {}
    # loop through the different sequences that appear in the fasta file
    # population dictionary with how many times that sequence appears
    for seq in set(concat_seq):
        average_d[seq] = (concat_seq.count(seq)/num_records)

    # intiailize list to hold the RCV values per ith taxa 
    # that will later be summed
    indiv_rcv_values = []

    # loop through records again and calculate RCV for 
    # each taxa and append to indivRCVvalues
    for record in alignment:
        # temp holds a temporary value of the numerator before appending
        # to numeratorRCVvalues and then is reassigned to 0 when it goes
        # through the loop again
        temp = 0
        # calculates the absolute value of the ith sequence letter minus the average
        for seq_letter in set(concat_seq):
            temp += abs(record.seq.count(seq_letter)-average_d[seq_letter])
        indiv_rcv_values.append(temp/(num_records*aln_len))

    # the sum of all RCV values
    return round(sum(indiv_rcv_values), 4)

def calc_saturation(alignment, tree):
    """
    calculate saturation
    """
    tips = []
    for tip in tree.get_terminals():
        tips.append(tip.name)

    combos = list(itertools.combinations(tips, 2))

    # for pairwise combinations, calculate patristic
    # distances and pairwise identities
    patristic_distances = []
    pairwise_identities = []
    aln_len = alignment.get_alignment_length()
    for combo in combos:
        # calculate pd
        patristic_distances.append(tree.distance(combo[0], combo[1]))
        # calculate pairwise identity
        identities = 0
        seq_one = ''
        seq_two = ''
        for record in alignment:
            if record.name == combo[0]:
                seq_one = record.seq
            elif record.name == combo[1]:
                seq_two = record.seq
        for idx in range(0, aln_len):
            if seq_one[idx] == seq_two[idx]:
                identities += 1
        pairwise_identities.append(identities / aln_len)

    # calculate linear regression
    _, _, r_value, _, _ = scipy.stats.linregress(pairwise_identities, patristic_distances)

    return round(r_value**2, 4)
