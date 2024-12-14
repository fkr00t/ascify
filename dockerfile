# Gunakan image dasar Python
FROM python:3.9-slim

# Tetapkan direktori kerja di dalam container
WORKDIR /app

# Salin file dari GitHub repository
RUN apt-get update && apt-get install -y git && \
    git clone https://github.com/fkr00t/ascify.git . && \
    apt-get remove -y git && apt-get autoremove -y

# Instal dependensi aplikasi
RUN pip install --no-cache-dir .

# Tetapkan entry point untuk command-line tool `ascify`
ENTRYPOINT ["ascify"]

# Tetapkan default argument (dapat diubah saat runtime)
CMD ["-h"]
