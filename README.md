# DoAnCloudNhom12
*Đồ án nhóm 12: tạo chương trình cho phép mở rộng ngôn ngữ biên dịch*

-Tải file về và unzip hoặc coppy tất cả các file vào 1 thư mục

-Cài đặt Docker trên máy

-Cài đặt python trên máy và thư viện tkinter và các thư viện khác

-Chạy tệp 'program.py', nhập chương trình cần biên dịch vào textbox sau đó nhận 'S...' và 'R...' ngôn ngữ cần biên dịch


*Chạy chương trình bằng docker images:(trên máy local)*

-Cài đặt x11 và khỏi động Xming

-Khởi động ddockerr và pull imange :19110418/doanclc về máy

  $ docker pull 19110418/doanclc:latest

-Sau đó run image với lệnh:

  $ docker run -it -v /var/run/docker.sock:/var/run/docker.sock 19110418/doanclc:latest

*Chạy trên máy ảo ec2:*

-Cài đặt PuTTY, xming, cấu hình  x11 trên máy ec2 theo các bước ở trang web: https://aws.amazon.com/vi/blogs/compute/how-to-enable-x11-forwarding-from-red-hat-enterprise-linux-rhel-amazon-linux-suse-linux-ubuntu-server-to-support-gui-based-installations-from-amazon-ec2/

-Coppy tất cả các file vào cùng 1 thư mục

-Cập nhập python và cài đặt thư viện tkinter

-Chạy file program.py bằng lệnh: $ python3 program.py
