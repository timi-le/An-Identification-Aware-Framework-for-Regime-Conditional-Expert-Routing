
from pathlib import Path
import shutil
from cmtf import synthetic_study
if __name__ == '__main__':
    root = Path(__file__).resolve().parent
    synthetic_study.main()
    output = root / 'results/cmtf'
    output.mkdir(parents=True, exist_ok=True)
    for path in (root/'cmtf').iterdir():
        if path.suffix in ('.csv', '.json'):
            shutil.copy(path, output/path.name)
    for extension in ('png', 'pdf'):
        name = 'synthetic_results.' + extension
        shutil.copy(root/'cmtf/assets'/name, root/'assets'/name)
