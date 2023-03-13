import numpy as np;

# Definindo Vetores
u =np.array([1,2]);
v = np.array([3,4]);

# Modulo de um vetor
np.linalg.norm(u);
print(np.linalg.norm(v));

#produto Escalar
v@u;
np.inner(u,v);
np.dot(u,v);
print(v@u);

#pela formula:  u.v = |u| x |v| x cos O = v1 x u1 + v2 x u2 + ... + un x vn
#cosseno:
cos = v@u/(np.linalg.norm(u) * np.linalg.norm(v));
print(cos);
#Cos em Radianos
cos = np.arccos(cos);
print(cos);
#Cos em graus
cos = np.rad2deg(cos);
print(cos);
