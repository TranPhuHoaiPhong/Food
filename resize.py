import cv2
import os

# Đặt thư mục ảnh gốc và thư mục lưu ảnh đã resize
images_dir = 'C:/Users/MSI/Downloads/food-101/food-101/images/waffles'  # Thư mục chứa ảnh gốc
resized_dir = 'C:/MainPlace/Study/MayHoc/Food/dataset/waffles'  # Thư mục lưu ảnh đã resize

# Tạo thư mục lưu ảnh đã resize nếu chưa tồn tại
os.makedirs(resized_dir, exist_ok=True)

# Kích thước mục tiêu (512x512)
target_size = (512, 512)

# Lặp qua tất cả ảnh trong thư mục
for image_name in os.listdir(images_dir):
    # Kiểm tra nếu tệp là ảnh (chỉ lấy các tệp có phần mở rộng .jpg hoặc .jpeg)
    if not image_name.lower().endswith(('.jpg', '.jpeg')):
        continue

    image_path = os.path.join(images_dir, image_name)
    
    # Đọc ảnh
    img = cv2.imread(image_path)
    
    # Kiểm tra nếu ảnh không được đọc đúng
    if img is None:
        print(f"Không thể đọc ảnh: {image_path}")
        continue  # Bỏ qua ảnh này và tiếp tục với ảnh khác

    # Lấy kích thước gốc của ảnh
    h, w = img.shape[:2]
    target_w, target_h = target_size

    # Tính tỷ lệ thay đổi để giữ tỷ lệ khung hình
    scale = min(target_w / w, target_h / h)

    # Resize ảnh sao cho giữ tỷ lệ khung hình
    new_w = int(w * scale)
    new_h = int(h * scale)
    resized_img = cv2.resize(img, (new_w, new_h))

    # Tạo background (padding) để đạt được kích thước target (512x512)
    top = (target_h - new_h) // 2
    bottom = target_h - new_h - top
    left = (target_w - new_w) // 2
    right = target_w - new_w - left

    # Thêm padding (background)
    padded_img = cv2.copyMakeBorder(resized_img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=(0, 0, 0))  # padding màu đen

    # Lưu ảnh đã được resize và padding
    resized_image_path = os.path.join(resized_dir, image_name)
    cv2.imwrite(resized_image_path, padded_img)

print("Resize và padding hoàn tất!")
