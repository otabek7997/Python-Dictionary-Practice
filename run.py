from data import randomuser_data
from randomusers import(
     get_full_names,
     get_users_by_country,
     count_users_by_gender
)


#print(get_users_by_country(randomuser_data,'Netherlands'))
print(count_users_by_gender(randomuser_data))