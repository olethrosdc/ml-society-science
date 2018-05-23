## -*- Mode: octave -*-

pkg load image;

X = double(imread("normal-brain.jpg")) / 256.0;
dims = size(X);
vec_size = size(vec(X));
n_data = 10;
n_class = 2;

data = zeros(n_data, vec_size);
target = zeros(n_data, 1);
for t=1:n_data
  data(t, :) = vec(X + imsmooth(randn(dims),"Gaussian", 8));
end

save ("fmriTrain.dat", "data", "target");

data = zeros(n_data, vec_size);
target = zeros(n_data, 1);
for t=1:n_data
  data(t, :) = vec(X + imsmooth(randn(dims),"Gaussian", 8));
end

save ("fmriTest.dat", "data", "target")
