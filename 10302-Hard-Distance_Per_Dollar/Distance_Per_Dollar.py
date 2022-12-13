# Import your libraries
import pandas as pd
# import the data
uber_request_logs=pd.read_csv('uber_request_logs.csv')
###uber_request_logs["request_date"]=uber_request_logs["request_date"].astype('datetime64')
uber_request_logs["request_date"] = pd.to_datetime(uber_request_logs["request_date"])
print(uber_request_logs)
# start writing code

## table 1 =
original_table = uber_request_logs[
    ["request_date", "distance_to_travel", "monetary_cost"]
]

original_table["request_date"] = original_table.request_date.apply(
    lambda t: t.strftime("%Y-%m")
)

## get the monthly average
avg_dpd_by_month = (
    original_table.groupby(["request_date"])["distance_to_travel", "monetary_cost"]
    .sum()
    .reset_index()
    .assign(
        monthly_avg_distance_per_dollar=lambda x: x.distance_to_travel / x.monetary_cost
    )
)[["request_date", "monthly_avg_distance_per_dollar"]]

original_table = (
    original_table.assign(
        date_avg_dist_per_dol=lambda x: x.distance_to_travel / x.monetary_cost
    )
)[["request_date", "date_avg_dist_per_dol"]]

## now we merge back the monthly average
res = original_table.merge(avg_dpd_by_month, on="request_date", how="left").assign(
    occurrence_count=lambda x: x.groupby(
        "request_date"
    ).monthly_avg_distance_per_dollar.transform("count"),
    abs_diff=lambda y: abs(y.date_avg_dist_per_dol - y.monthly_avg_distance_per_dollar),
)

occur = res.drop_duplicates(subset=["request_date"])[
    ["request_date", "occurrence_count"]
]

ans = res.groupby("request_date")["abs_diff"].sum().reset_index()

ans = (
    ans.merge(occur, on="request_date", how="left")
    .assign(mean_deviation=lambda x: x.abs_diff / x.occurrence_count)
    .round(2)
)

ans[["request_date", "mean_deviation"]]

print(ans)