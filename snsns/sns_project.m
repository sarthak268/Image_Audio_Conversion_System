%%
% This part simply converts the mp3 files to .wav files 

filename = '/Users/sarthakbhagat/Desktop/sns/test.mp3';
signal = audioread(filename);

wavFileName = '/Users/sarthakbhagat/Desktop/sns/test.wav';
audiowrite(wavFileName, signal, 44100);

%info = audioinfo(filename);
%disp('Sampling rate is ');
%disp(info.SampleRate);

%[y,fs] = audioread('/Users/sarthakbhagat/Desktop/sns/test.wav');
%plot(y);

%%
% size of the image

[y,fs] = audioread('/Users/sarthakbhagat/Desktop/sns/test.wav');

sw = size(y);
sw_each = sw/3;
rc_each = sqrt(sw_each);
rc_each = floor(rc_each);

%%
% convert the column vector into m*n matrix

[y,fs] = audioread('/Users/sarthakbhagat/Desktop/sns/test.wav');
y = y(1:7680000);

image = zeros(1600,1600,3);

a = 1;
b = 1;

index = 1;
for i = 1:1600
    for j = 1:1600
        for k = 1:3
            image(i, j, k) = y(index);
            index = index + 1;
        end
    end
end

imwrite(image,'/Users/sarthakbhagat/Desktop/sns/test.jpg');
imwrite(image,'/Users/sarthakbhagat/Desktop/sns/test.png');
imwrite(image,'/Users/sarthakbhagat/Desktop/sns/test.jpeg');


%imshow('/Users/sarthakbhagat/Desktop/sns/test.jpg');


%%
% image to column vector 

im = imread('/Users/sarthakbhagat/Desktop/sns/test.jpg');
sz = size(im);

aud = zeros(sz(1)*sz(2)*sz(3),1);
ind = 1;

for i = 1:sz(1)
    for j = 1:sz(2)
        for k = 1:sz(3)
            aud(ind) = im(i,j,k);
            ind = ind + 1;
        end
    end 
end

sound(aud,44100[y,fs] = audioread('/Users/sarthakbhagat/Desktop/sns/test.wav');
);
%later add fs



