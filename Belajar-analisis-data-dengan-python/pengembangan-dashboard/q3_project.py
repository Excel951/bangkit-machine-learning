q3_df = hour_df
rush_hour_df = q3_df.groupby(by='hr').cnt.sum().sort_values(ascending=False).reset_index()
rush_hour_df['hour'] = rush_hour_df.hr.apply(lambda x: str(x)+' a.m.' if x >= 0 and x < 12 else str(x-12)+' p.m.')

rush_hour_df.rename(columns={
    'cnt': 'total_rentals'
}, inplace=True)
plt.figure(figsize=(10,5))
colors_ = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(x='total_rentals', y='hour', data=rush_hour_df.head(5), palette=colors_)
plt.title("Rush Hour in Bike Rentals", loc='center', fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='y', labelsize=12)
plt.show()