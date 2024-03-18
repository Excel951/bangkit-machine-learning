q4_df = hour_df

# Memilih fitur
kmeans_clustering_parameter = q4_df[['cnt', 'hr']]  # Memilih jumlah peminjaman dan jam

# Melakukan clustering dengan K-Means
kmeans = KMeans(n_clusters=3)  # Misalnya, kita ingin melakukan clustering menjadi 3 kelompok
kmeans.fit(kmeans_clustering_parameter)

# Menambahkan label cluster ke DataFrame
q4_df['cluster'] = kmeans.labels_

# Visualisasi hasil clustering
plt.figure(figsize=(10, 6))
for cluster in sorted(q4_df['cluster'].unique()):
    cluster_data = q4_df[q4_df['cluster'] == cluster]
    plt.scatter(cluster_data['hr'], cluster_data['cnt'], label=f'Kelompok Customer {cluster+1}')

plt.xlabel('Hour')
plt.ylabel('Total of Bike Rentals')
plt.title('Clustering of Bike Rental Patterns')
plt.legend()
plt.show()