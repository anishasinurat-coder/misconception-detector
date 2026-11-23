from pathlib import Path

file = Path(__file__).parent / "app.py"

kode = file.read_text(encoding="utf-8")
jumlah = kode.count("\u00a0")
kode = kode.replace("\u00a0", " ")
file.write_text(kode, encoding="utf-8")

print(f"Berhasil membersihkan {jumlah} spasi khusus.")

