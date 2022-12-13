# Import your libraries
import pandas as pd
# import the data
fb_friend_requests = pd.read_csv('fb_friend_requests.csv')
print(fb_friend_requests)
# Start writing code
#fb_friend_requests.head()

#splitting data into sent and accepted
fb_friend_sent = fb_friend_requests[fb_friend_requests.action=="sent"]
fb_friend_accepted = fb_friend_requests[fb_friend_requests.action=="accepted"]

#merging the data to bring sent and accepted in a single row for userid, received id combination
merged_df = pd.merge(fb_friend_sent, fb_friend_accepted,  how='left', left_on=['user_id_sender','user_id_receiver'], right_on = ['user_id_sender','user_id_receiver'])


#grouping the data based on the request sent
grouped_df = merged_df.groupby(['date_x']).agg(['count'])#.reset_index()

#converting the grouped data into dataframe
grouped_df.columns = [ ' '.join(str(i) for i in col) for col in grouped_df.columns]
grouped_df.reset_index(inplace=True)


#creating a new column in grouped data to find ratio between accepted/sent request
grouped_df['acceptance_rate'] = grouped_df['action_y count']/grouped_df['action_x count']

#subsetting columns to show date vs acceptance rate
final_df = grouped_df[['date_x','acceptance_rate']]

final_df.head()
print(final_df)
