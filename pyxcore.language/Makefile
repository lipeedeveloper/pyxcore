# PyxCore Makefile
.PHONY: all clean test compile-examples help install

# Directories
COMPILER_DIR = compiler
EXAMPLES_DIR = examples
VSCODE_EXT_DIR = vscode-extension
BUILD_DIR = build

help:
	@echo "PyxCore Build System"
	@echo "===================="
	@echo "Targets:"
	@echo "  make compile-examples   - Compile all example programs"
	@echo "  make test               - Run tests"
	@echo "  make clean              - Remove generated files"
	@echo "  make install            - Install PyxCore"
	@echo "  make help               - Show this help message"

compile-examples:
	@echo "[*] Compiling examples..."
	@mkdir -p $(BUILD_DIR)
	@python3 $(COMPILER_DIR)/pyxc.py $(EXAMPLES_DIR)/hello.pyx -o $(BUILD_DIR)/hello
	@python3 $(COMPILER_DIR)/pyxc.py $(EXAMPLES_DIR)/functions.pyx -o $(BUILD_DIR)/functions
	@python3 $(COMPILER_DIR)/pyxc.py $(EXAMPLES_DIR)/classes.pyx -o $(BUILD_DIR)/classes
	@python3 $(COMPILER_DIR)/pyxc.py $(EXAMPLES_DIR)/pattern_match.pyx -o $(BUILD_DIR)/pattern_match
	@python3 $(COMPILER_DIR)/pyxc.py $(EXAMPLES_DIR)/error_handling.pyx -o $(BUILD_DIR)/error_handling
	@python3 $(COMPILER_DIR)/pyxc.py $(EXAMPLES_DIR)/db_example.pyx -o $(BUILD_DIR)/db_example
	@echo "[+] Examples compiled in $(BUILD_DIR)/"

test:
	@echo "[*] Running tests..."
	@python3 -m pytest tests/ -v

clean:
	@echo "[*] Cleaning up..."
	@rm -rf $(BUILD_DIR) *.c *.o *.exe
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -delete
	@echo "[+] Clean complete"

install:
	@echo "[*] Installing PyxCore..."
	@chmod +x $(COMPILER_DIR)/pyxc.py
	@echo "[+] PyxCore installed. Add to PATH or use: python $(COMPILER_DIR)/pyxc.py"

format:
	@echo "[*] Formatting Python code..."
	@python3 -m black $(COMPILER_DIR)/ --line-length 88

lint:
	@echo "[*] Linting Python code..."
	@python3 -m flake8 $(COMPILER_DIR)/ --max-line-length 88

package:
	@echo "[*] Packaging release artifact..."
	@python - <<'PY'
import os, zipfile
root = os.getcwd()
archive = os.path.join(root, 'dist', 'pyxcore.zip')
os.makedirs(os.path.dirname(archive), exist_ok=True)
with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as z:
    for folder, _, files in os.walk(root):
        if folder.startswith(os.path.join(root, '.git')): continue
        if 'dist' in folder.split(os.sep): continue
        for file in files:
            if file.endswith('.pyc') or file == 'test_output.txt':
                continue
            path = os.path.join(folder, file)
            arcname = os.path.relpath(path, root)
            z.write(path, arcname)
print(f'Created package: {archive}')
PY

docs:
	@echo "[*] Documentation is available in README.md, GETTING_STARTED.md, INSTALL.md, REFERENCE.md, PROJECT_SUMMARY.md, DELIVERY.md"

.DEFAULT_GOAL := help
