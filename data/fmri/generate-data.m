## -*- Mode: octave -*-

X = double(imread("normal-brain.jpg")) / 256.0;
dims = size(X);
vec_size = size(vec(X));
n_data = 100;
n_class = 2;

data = zeros(n_data + 1, vec_size)
target = zeros(n_data, 1);
for i=1:n_data
  
end

save ("fmriTrain.dat", "data", "target")

data = zeros(n_data + 1, vec_size)
target = zeros(n_data, 1);
for i=1:n_data
  
end

save ("fmriTest.dat", "data", "target")
