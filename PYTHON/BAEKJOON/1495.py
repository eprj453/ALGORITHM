from pprint import pprint

N, S, M = map(int, input().split())
volumes = list(map(int, input().split()))

available_volume = [[0] * (M+1) for _ in range(N+1)]
available_volume[0][S] = 1
max_volume = 0


for i in range(1, N+1):
    volume = volumes[i-1]
    for j in range(M+1):
        if available_volume[i-1][j]:
            if j - volume >= 0:
                available_volume[i][j-volume] = 1
            if j + volume <= M:
                available_volume[i][j+volume] = 1



# print(available_volume

max_volume = -1
for i in range(M+1):
    if available_volume[-1][i]:
        max_volume = i

print(max_volume)
# def change_volume(current_volume, song_idx):
#     global max_volume

#     print(f'song_idx : {song_idx}')

#     if song_idx >= len(songs):
#         print('ss')
#         max_volume = max(current_volume, max_volume)
#         return
    
#     idx_volume = songs[song_idx]

#     if current_volume + idx_volume <= M:
#         change_volume(current_volume+idx_volume, song_idx+1)
#     if current_volume - idx_volume >= 0:
#         change_volume(current_volume-idx_volume, song_idx+1)

# change_volume(S, 0)
# print(max_volume)

