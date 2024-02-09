#include <stdio.h>
#include <errno.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/stat.h>

enum {
    RET_NO_ERROR,
    RET_INPUT_ERROR,
    RET_OUTPUT_ERROR,
    RET_USAGE,
    RET_MEMORY_ERROR
};

int main(int argc, char* argv[]) {
    int fi = -1;
    int fo = -1;
    unsigned char* buffer = NULL;
    off_t i;
    off_t offset;
    off_t fsize;
    off_t file_size;
    ssize_t nread;
    ssize_t nwrite;
    int ret;
    struct stat st;
    int rc;

    // Check parameters
    if (argc != 3) {
        fprintf(stderr, "Usage: %s <input BMP file> <output BMP file>\n", argv[0]);
        ret = RET_USAGE;
        goto end;
    }

    // Open input file in read-only mode
    fi = open(argv[1], O_RDONLY);
    if (fi < 0) {
        fprintf(stderr, "Unable to open input file: %d\n", errno);
        ret = RET_INPUT_ERROR;
        goto end;
    }

    // Get input file size
    rc = fstat(fi, &st);
    if (rc < 0) {
        fprintf(stderr, "Unable to get stats of input file: %d\n", errno);
        ret = RET_INPUT_ERROR;
        goto end;
    }
    file_size = st.st_size;

    // Check the minimal size of inoput file (BMP header len)
    if (file_size < 14) {
        fprintf(stderr, "Input file is too small: %lld\n", file_size);
        ret = RET_INPUT_ERROR;
        goto end;
    }

    // Allocate memory for the input file content
    buffer = malloc(file_size);
    if (buffer == NULL) {
        fprintf(stderr, "Unable to allocate memory: %lld\n", file_size);
        ret = RET_MEMORY_ERROR;
        goto end;
    }

    // Read input file
    nread = read(fi, buffer, file_size);
    if (nread != file_size) {
        fprintf(stderr, "Error during data reading from the input file: %d\n", errno);
        ret = RET_INPUT_ERROR;
        goto end;
    }

    // Check magic pattern (BM)
    if (buffer[0] != 'B' || buffer[1] != 'M') {
        fprintf(stderr, "Not a BMP file\n");
        ret = RET_INPUT_ERROR;
        goto end;
    }

    // Check the size in the BMP header
    fsize = buffer[2];
    fsize |= buffer[3] << 8;
    fsize |= buffer[4] << 16;
    fsize |= buffer[5] << 24;

    if (fsize != file_size) {
        fprintf(stderr, "Size is invalid: %lld/%lld\n", fsize, file_size);
        ret = RET_INPUT_ERROR;
        goto end;
    }

    // Get data offset from the BMP header
    offset = buffer[10];
    offset |= buffer[11] << 8;
    offset |= buffer[12] << 16;
    offset |= buffer[13] << 24;

    // Check offset value
    if (offset > file_size) {
        fprintf(stderr, "Offset is invalid: %lld/%lld\n", offset, file_size);
        ret = RET_INPUT_ERROR;
        goto end;
    }

    // Extract the hidden image by replacing the original one
    for (i = offset; i < file_size;i++) {
        buffer[i] <<= 4;
    }

    // Open the output file in write-only mode
    fo = open(argv[2], O_CREAT | O_WRONLY, 0666);
    if (fo < 0) {
        fprintf(stderr, "Unable to open output file: %d\n", errno);
        ret = RET_OUTPUT_ERROR;
        goto end;
    }

    // Write the extracted image
    nwrite = write(fo, buffer, file_size);
    if (nwrite != file_size) {
        fprintf(stderr, "Error during data writing into output file: %d\n", errno);
        ret = RET_OUTPUT_ERROR;
        goto end;
    }

    ret = RET_NO_ERROR;

end:
    // Clean allocated resources
    if (fi != -1)
        close(fi);
    if (fo != -1)
        close(fo);
    if (buffer != NULL)
        free(buffer);

    return ret;
}
