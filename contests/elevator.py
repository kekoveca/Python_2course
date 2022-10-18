N, M, K, Ta, Tb, Tc = input().split(" ")
N, M, K, Ta, Tb, Tc = int(N), int(M), int(K), float(Ta), float(Tb), float(Tc)
delta = abs(M - N)
timePeshkom = Tc * delta

timeLift = abs(K - N) + 3*Tb + delta*Ta

if timeLift <= timePeshkom:
    print("elevator")
else:
    print("stairs")