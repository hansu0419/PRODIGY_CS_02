from flask import Flask, request, render_template, send_file, redirect, url_for
from PIL import Image
import random
import io

app = Flask(__name__)

def decrypt_image(input_image, seed):
    img = Image.open(io.BytesIO(input_image))
    img = img.convert("RGB")
    pixels = img.load()
    width, height = img.size
    
    shuffled_pixels = [[pixels[x, y] for x in range(width)] for y in range(height)]
    unshuffled_pixels = unshuffle_pixels(shuffled_pixels, width, height, seed)

    decrypted_img = Image.new("RGB", (width, height))
    decrypted_pixels = decrypted_img.load()
    for y in range(height):
        for x in range(width):
            decrypted_pixels[x, y] = swap_channels(unshuffled_pixels[y][x])
    
    byte_io = io.BytesIO()
    decrypted_img.save(byte_io, format='PNG')
    byte_io.seek(0)
    return byte_io

def swap_channels(pixel):
    r, g, b = pixel
    return (b, g, r)

def unshuffle_pixels(shuffled_pixels, width, height, seed):
    pixel_list = [pixel for row in shuffled_pixels for pixel in row]
    
    indices = list(range(width * height))
    unshuffled_indices = indices[:]
    random.seed(seed)
    random.shuffle(unshuffled_indices)
    
    unshuffled_pixel_list = [None] * (width * height)
    for i, index in enumerate(unshuffled_indices):
        unshuffled_pixel_list[index] = pixel_list[i]
    
    unshuffled_pixels = []
    for i in range(height):
        start_index = i * width
        end_index = start_index + width
        unshuffled_pixels.append(unshuffled_pixel_list[start_index:end_index])
    
    return unshuffled_pixels

def encrypt_image(input_image, seed):
    img = Image.open(io.BytesIO(input_image))
    img = img.convert("RGB")
    pixels = img.load()
    width, height = img.size
    
    for y in range(height):
        for x in range(width):
            pixels[x, y] = swap_channels(pixels[x, y])
    
    shuffled_pixels = shuffle_pixels(pixels, width, height, seed)
    encrypted_img = Image.new("RGB", (width, height))
    encrypted_pixels = encrypted_img.load()
    for y in range(height):
        for x in range(width):
            encrypted_pixels[x, y] = shuffled_pixels[y][x]
    
    byte_io = io.BytesIO()
    encrypted_img.save(byte_io, format='PNG')
    byte_io.seek(0)
    return byte_io

def shuffle_pixels(pixels, width, height, seed):
    pixel_list = [pixels[x, y] for y in range(height) for x in range(width)]
    
    random.seed(seed)
    
    indices = list(range(width * height))
    shuffled_indices = indices[:]
    random.shuffle(shuffled_indices)
    
    shuffled_pixel_list = [pixel_list[i] for i in shuffled_indices]
    
    shuffled_pixels = []
    for i in range(height):
        start_index = i * width
        end_index = start_index + width
        shuffled_pixels.append(shuffled_pixel_list[start_index:end_index])
    
    return shuffled_pixels

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        action = request.form.get('action')
        seed = request.form.get('seed')
        if not seed.isdigit():
            return "Seed must be an integer.", 400
        seed = int(seed)

        file = request.files.get('file')
        if not file:
            return "No file provided.", 400
        
        image_data = file.read()
        
        if action == 'Encrypt':
            encrypted_img = encrypt_image(image_data, seed)
            return send_file(encrypted_img, mimetype='image/png', as_attachment=True, download_name='encrypted_image.png')
        elif action == 'Decrypt':
            decrypted_img = decrypt_image(image_data, seed)
            return send_file(decrypted_img, mimetype='image/png', as_attachment=True, download_name='decrypted_image.png')
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
