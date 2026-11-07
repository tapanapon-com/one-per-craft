# ติดตั้งบน Mac / macOS installation

เลือกแอปจาก [ตารางรวม](../README.md#แอปทั้งหมดและ-github-แยก) หรือ [เว็บไซต์](https://tapanapon.com/one-per-craft) โดยแยกต้นฉบับล่าสุดจากรุ่นไทยที่มีจริง 3 แอป

1. ตรวจ Chip และ macOS version จาก Apple → About This Mac
2. เปิด GitHub Releases ของแอปและรุ่นที่ต้องการ ขยาย Assets แล้วเลือก DMG ตามข้อกำหนดระบบ
3. Source code ZIP/tar.gz ต้อง build ก่อน ไม่ใช่แอปพร้อมเปิด
4. บันทึกงานและปิดแอปเดิม เปิด DMG แล้วลากแอปไป Applications
5. Eject ดิสก์ติดตั้ง เปิดจาก Applications และตรวจ SHA-256 ของรุ่นเดียวกัน

รุ่นไทยที่เผยแพร่แล้วเป็น Apple Silicon (arm64) และมีสถานะการเซ็นแยกจากต้นฉบับ ส่วนต้นฉบับใน snapshot ปัจจุบันมี Universal DMG ให้เลือก อ่านข้อจำกัดการเซ็น/ระบบจาก Release นั้นโดยตรง

[คู่มือฉบับเต็มบนเว็บ](https://tapanapon.com/blog/one-per-craft-install-mac-github)

## English

Choose a real published Thai release or the current upstream release, check chip/OS requirements, select its DMG in Release Assets, verify the matching checksum and drag the app into Applications. Source archives require a build. The three Thai releases and upstream Universal packages have different architecture/signing notes; read the selected release's instructions.
