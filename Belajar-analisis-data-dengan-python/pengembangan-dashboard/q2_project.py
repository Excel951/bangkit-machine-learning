q2_df = day_df
q2_df['weather_name'] = q2_df.weathersit.apply(lambda x: "Clear, Few clouds, Partly cloudy" if x == 1 else ("Mist, Cloudy, Broken clouds" if x == 2 else ("Light Snow, Light Rain, Thunderstorm, Scattered clouds" if x == 3 else "Heavy Rain, Ice Pallets, Thunderstorm, Mist, Snow, Fog")))
weather_most_liked_df = q2_df.groupby(by='weather_name').cnt.sum().sort_values(ascending=False).reset_index()

colors = ["#72BCD4", "#D3D3D3", "#D3D3D3"]

plt.figure(figsize=(10, 5))
sns.barplot(x='cnt', y='weather_name', data=weather_most_liked_df.head(), palette=colors)
plt.ylabel(None)
plt.xlabel(None)
plt.title("Weather Most Favored by Customers", loc='center', fontsize=15)
# plt.tick_params(axis='y', labelsize=12)
for index, value in enumerate(weather_most_liked_df.head()['cnt']):
    if value < 500000:
        continue
    plt.text(value, index, str(value), ha='right', va='center')
plt.show()