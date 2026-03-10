import os, csv

base_input = os.path.join('data')
base_output = 'trasposed_data'

processed = []
for root, dirs, files in os.walk(base_input):
    # Skip the analisis root itself (only process files inside subfolders)
    if root == base_input:
        continue
    for fname in files:
        if not fname.endswith('.txt'):
            continue
        in_path = os.path.join(root, fname)
        rel = os.path.relpath(in_path, base_input)
        out_path = os.path.join(base_output, rel)
        os.makedirs(os.path.dirname(out_path), exist_ok=True)

        with open(in_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='\t')
            data = [row for row in reader]

        if not data:
            continue

        # Transpose: rows become columns, columns become rows
        transposed = list(map(list, zip(*data)))

        with open(out_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f, delimiter='\t')
            writer.writerows(transposed)

        processed.append(out_path)
        print(f'Transposed: {in_path} -> {out_path}')

print(f'Done: {len(processed)} file(s) processed.')