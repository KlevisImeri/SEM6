import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

FILE_NAME = "entity_prevalence.csv"
NUM_TOP_ENTITIES = 10
CHART_WIDTH = 20
CHART_HEIGHT = 20
TITLE_FONT_SIZE = 20
TITLE_PADDING = 20
X_AXIS_LIMIT_MIN = 0
X_AXIS_LIMIT_MAX = 1.0
GRID_ALPHA = 0.7
SAVE_DPI = 300
BAR_ROUNDNESS = 0.4
TRACKING_COLOR = '#66b3ff'
NONTRACKING_COLOR = '#ff9999'

df = pd.read_csv(FILE_NAME)
df = df.head(NUM_TOP_ENTITIES)
df['Entity'] = df['Entity'].str.replace('"', '')
df = df.sort_values('Tracking Prevalence')

plt.figure(figsize=(CHART_WIDTH, CHART_HEIGHT))

bars_tracking = plt.barh(
    df['Entity'],
    df['Tracking Prevalence'],
    color=TRACKING_COLOR,
    label='Tracking Prevalence',
    edgecolor='grey',
    linewidth=0.5,
    height=0.8,
    capstyle='round',
    xerr=0,
    align='center'
)

bars_nontracking = plt.barh(
    df['Entity'],
    df['Non-tracking Prevalence'],
    left=df['Tracking Prevalence'],
    color=NONTRACKING_COLOR,
    label='Non-tracking Prevalence',
    edgecolor='grey',
    linewidth=0.5,
    height=0.8,
    capstyle='round',
    xerr=0,
    align='center'
)


for bar in bars_tracking + bars_nontracking:
    bar.set_width(bar.get_width())
    bar.set_height(bar.get_height())
    bar.set_xy(bar.get_xy())
    bar.set_capstyle('round')
    bar.set_linewidth(0.5)
    bar.set_edgecolor('grey')

for i, (entity, tracking, nontracking) in enumerate(
    zip(
        df['Entity'],
        df['Tracking Prevalence'],
        df['Non-tracking Prevalence']
    )
):
    total = tracking + nontracking
    plt.text(
        total + 0.01,
        i,
        f'{total:.1%}',
        va='center'
    )

plt.xlabel('Prevalence (%)')
plt.title(
    'Source of the Most Common Trackers Found on Top 145K Websites',
    fontsize=TITLE_FONT_SIZE,
    pad=TITLE_PADDING
)
plt.xlim(X_AXIS_LIMIT_MIN, X_AXIS_LIMIT_MAX)
plt.grid(axis='x', linestyle='--', alpha=GRID_ALPHA)
plt.legend(loc='upper right')
plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(
    lambda x, _: f'{x:.0%}'
))
plt.subplots_adjust(top=0.952, bottom=0.043, left=0.163, right=0.973, hspace=0.205, wspace=0.23)
plt.tight_layout()
plt.show()
