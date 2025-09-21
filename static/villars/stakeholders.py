import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Arial"

## Positions
stakeholders = [
    {"name": "Scientific\ncommunity", "status_quo": 4, "involvement": 8.75, "power": 3, "type": "Civil society"},
    {"name": "Environmental\nNGOs", "status_quo": 4, "involvement": 7, "power": 2, "type": "Civil society"},
    {"name": "Youth &\nstudents", "status_quo": 3, "involvement": 2, "power": 1, "type": "Civil society"},
    {"name": "Signatories\nwith claims", "status_quo": 1, "involvement": 9, "power": 4, "type": "States"},
    {"name": "Signatories with\nrights to claim", "status_quo": -2, "involvement": 8.5, "power": 5, "type": "States"},
    {"name": "Other signatories\nwithout claims", "status_quo": 3, "involvement": 8, "power": 5, "type": "States"},
    {"name": "Non-signatory\nstates", "status_quo": 1, "involvement": 1, "power": 1, "type": "States"},
    {"name": "Tourism\nindustry", "status_quo": 0.5, "involvement": 6, "power": 1, "type": "Industries"},
    {"name": "Fishing\nindustry", "status_quo": -2, "involvement": 5, "power": 2, "type": "Industries"},
    {"name": "Mining\nindustry", "status_quo": -3, "involvement": 4, "power": 3, "type": "Industries"},
    {"name": "United\nNations", "status_quo": 3, "involvement": 6, "power": 3, "type": "International bodies"},
    {"name": "Antarctic Treaty\nSecretariat", "status_quo": 3.5, "involvement": 9.5, "power": 1, "type": "International bodies"}
]

## Categories
category_colors = {
    "Civil society": "tab:green",
    "States": "tab:orange",
    "Industries": "tab:red",
    "International bodies": "tab:blue",
}

## Plotting
fig, ax = plt.subplots(figsize=(9, 9))

for s in stakeholders:
    ax.scatter(
        s["status_quo"], s["involvement"],
        s=s["power"] * 300,
        color=category_colors[s["type"]],
        edgecolors="black", linewidth=1
    )
    ax.text(
        s["status_quo"] + 0.18 + s["power"] * 0.05,
        s["involvement"] - 0.16,
        s["name"], fontsize=9
    )

## Axes
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.set_xlim(-4.25, 5.75)
ax.set_ylim(0, 10)
ax.set_xticks([-4, -2, 0, 2, 4])
ax.set_yticks([2, 4, 6, 8, 10])
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.set_xlabel("Challenge Treaty ↔ Maintain the Peaceful Status Quo")
ax.set_ylabel("Involvement")

## Legend
handles = [
    plt.Line2D([0], [0], marker='o', color='w', label=cat,
               markerfacecolor=color, markersize=10, markeredgecolor="black")
    for cat, color in category_colors.items()
]
ax.legend(handles=handles, bbox_to_anchor=(0, 0), loc='lower left')

## Save figure
plt.savefig("stakeholders.png", dpi=500)
