clear;

%initialize input image
pixels = [0,1,0,0;
          1,0,0,0;
          0,0,1,0;
          0,1,0,1;
          0,0,1,0];
pixels

%initialize meta variables
h_in = 5;
w_in = 4;
input_n.data = pixels;
input_n.height = h_in;
input_n.width = w_in;
input_n.channel = 1;
input_n.data

%use a kernel of size 2x2 with no padding and stride of 1
layer.k = 2;
layer.pad = 0;
layer.stride = 1;

h_out = (h_in + 2*layer.pad - layer.k) / layer.stride + 1;
w_out = (w_in + 2*layer.pad - layer.k) / layer.stride + 1;

%number of convolution kernels
numFilters = 1;
param.w = [0,1;
           1,0];
       
%display weights and reshape them to column vector       
param.w
param.w = reshape(param.w, layer.k*layer.k*input_n.channel, numFilters);
param.w

%convert input image to col space
col = im2col_conv(input_n, layer, h_out, w_out);
col = reshape(col, layer.k*layer.k*input_n.channel, h_out*w_out);

%convolution operation
output_n.data = col'*param.w;
output_n.data
reshape(output_n.data, h_out, w_out, numFilters)


%derivative of output w.r.t input is just the convolution kernel but summed
%up across all windows. Can achieve this with repmat and col2im_conv
col_diff = repmat(param.w, 1, h_out*w_out);
im = col2im_conv(col_diff(:), input_n, layer, h_out, w_out)
input_od = im(:);