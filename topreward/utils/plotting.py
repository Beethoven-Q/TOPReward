"""Plotting utilities for TOPReward results."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from topreward.results.prediction import InstructionRewardRecord


def plot_normalized_progress_reward(record: InstructionRewardRecord, output_dir: Path) -> None:
    """Plot normalized progress reward vs trajectory progress for a single record.

    Saves to {output_dir}/example_0_progress_reward.png.
    """
    if record.prefix_lengths is None or record.normalized_log_probs is None:
        return

    x = [l / record.num_frames for l in record.prefix_lengths]
    y = record.normalized_log_probs

    fig, ax = plt.subplots()
    ax.plot(x, y, marker="o", linewidth=1.5, markersize=4)
    ax.set_xlabel("Trajectory progress")
    ax.set_ylabel("Normalized reward")
    title = record.instruction
    if record.voc is not None:
        title += f"\nVOC={record.voc:.4f}"
    ax.set_title(title, wrap=True)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    output_path = Path(output_dir) / "example_0_progress_reward.png"
    fig.savefig(output_path, bbox_inches="tight")
    plt.close(fig)


def plot_exponentiated_progress_reward(record: InstructionRewardRecord, output_dir: Path) -> None:
    """Plot exponentiated (exp) normalized progress reward vs trajectory progress for a single record.

    Saves to {output_dir}/example_0_progress_reward_exp.png.
    """
    if record.prefix_lengths is None or record.normalized_log_probs is None:
        return

    x = [l / record.num_frames for l in record.prefix_lengths]
    y = list(np.exp(record.normalized_log_probs))

    fig, ax = plt.subplots()
    ax.plot(x, y, marker="o", linewidth=1.5, markersize=4)
    ax.set_xlabel("Trajectory progress")
    ax.set_ylabel("Normalized probability")
    title = record.instruction
    if record.voc is not None:
        title += f"\nVOC={record.voc:.4f}"
    ax.set_title(title, wrap=True)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    output_path = Path(output_dir) / "example_0_progress_reward_exp.png"
    fig.savefig(output_path, bbox_inches="tight")
    plt.close(fig)
