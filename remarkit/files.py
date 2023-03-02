import csv

import matplotlib.pyplot as plt


def read_input_file(input:str) -> list:
    """
    reads input three column file
    """
    return [[s for s in l.split()] for l in open(input).readlines()]

def output_information_content(
        merged_df: list,
        output_file: str,
):
    with open(output_file+".txt", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["identifiers", "overall_desirability", "treeness_over_rcv_desirabilities", "saturation_desirabilities", "treeness_desirabilities", "treeness_over_rcv", "saturation", "treeness"]) 
        writer.writerows(merged_df)  

def output_plot(
        merged_df:list,
        output_file:str,
        plot: str,
):
    
    plt.figure(figsize=(8, len(merged_df)*.2), dpi=80)

    plt.axvline(0.25, color='#D3D3D3', linestyle='solid', linewidth=1, zorder=0)
    plt.axvline(0.50, color='#D3D3D3', linestyle='solid', linewidth=1, zorder=0)
    plt.axvline(0.75, color='#D3D3D3', linestyle='solid', linewidth=1, zorder=0)

    plt.xticks(ticks=[0.00, 0.25, 0.50, 0.75, 1.00], labels=[0.00, 0.25, 0.50, 0.75, 1.00])
    plt.hlines(y=list(list(zip(*merged_df))[0]), xmin=0, xmax=list(list(zip(*merged_df))[1]), color='#9C9C9C', zorder=0)
    plt.scatter(list(list(zip(*merged_df))[4]), list(list(zip(*merged_df))[0]), color="#009E73", alpha=0.5, label = "Treeness", zorder=5)
    plt.scatter(list(list(zip(*merged_df))[3]), list(list(zip(*merged_df))[0]), color="#D55E00", alpha=0.5, label = "Saturation", zorder=10)
    plt.scatter(list(list(zip(*merged_df))[2]), list(list(zip(*merged_df))[0]), color="#0072B2", alpha=0.5, label = "Treeness / RCV", zorder=15)
    plt.scatter(list(list(zip(*merged_df))[1]), list(list(zip(*merged_df))[0]), color="#535353", alpha=1.0, label = "Overall", zorder=20)
    plt.gca().invert_yaxis()
    handles, labels = plt.gca().get_legend_handles_labels()
    order = [3, 2, 1, 0]
    legend = plt.legend([handles[idx] for idx in order],[labels[idx] for idx in order], loc = "lower right")
    legend.get_frame().set_alpha(1)
    plt.xlabel("Desirability")

    if plot:
        if plot == "png":
            plt.savefig(output_file+".png")
        else:
            plt.savefig(output_file+".svg")

    plt.clf()
