# Import your libraries
import pandas as pd
# import the data
google_gmail_emails = pd.read_csv('google_gmail_emails.csv')
print(google_gmail_emails)
# start writing code
user_with_count = (
    google_gmail_emails.groupby(["from_user"])["id"].count().to_frame().reset_index()
)

result = (
    user_with_count.assign(rank=lambda x: x.id.rank(method="first", ascending=False))
    .sort_values(by=["id", "from_user"], ascending=[False, True])
    .rename(columns={"id": "total_emails"})
)
print(result)