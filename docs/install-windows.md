# ติดตั้งบน Windows / Windows installation

เลือกแอปและรุ่นจาก [README](../README.md) หรือ [เว็บไซต์](https://tapanapon.com/one-per-craft) โดยแยกต้นฉบับจากแพ็กเกจไทย

- **MSI:** ปิดแอปเดิม เปิดตัวติดตั้ง ทำตามหน้าจอ แล้วเปิดผ่าน Start Menu
- **Portable ZIP:** ใช้ Extract All แตกไฟล์ทั้งหมดลงโฟลเดอร์ที่เขียนได้ แล้วเปิด `.exe` ของแอป เก็บไฟล์ประกอบไว้ครบ
- เลือก x64, ARM64 หรือ x86 ให้ตรงกับเครื่องและการรองรับของต้นทาง
- ตรวจ SHA-256 โดยใช้รายการชื่อไฟล์และ Release เดียวกัน ไม่ใช้ hash ของ ZIP มาเทียบ MSI
- Source code ZIP ไม่ใช่ตัวติดตั้ง; ไฟล์ symbols เป็นข้อมูลสำหรับวิเคราะห์ปัญหา

[คู่มือ MSI/Portable/GitHub ฉบับเต็ม](https://tapanapon.com/blog/one-per-craft-install-windows-github)

## รุ่นไทยที่ตรวจแล้ว

| แอป | รุ่น | ดาวน์โหลดและ SHA-256 |
| --- | --- | --- |
| PhotoCraft | 0.21.0-th.1 | [Release พร้อมไฟล์และ checksums](https://github.com/tapanapon-com/photocraft-th/releases/tag/v0.21.0-th.1) |
| VectorCraft | 0.22.0-th.1 | [Release พร้อมไฟล์และ checksums](https://github.com/tapanapon-com/vectorcraft-th/releases/tag/v0.22.0-th.1) |
| FilmCraft | 0.18.0-th.1 | [Release พร้อมไฟล์และ checksums](https://github.com/tapanapon-com/filmcraft-th/releases/tag/v0.18.0-th.1) |

รุ่นไทยรอบนี้เป็น Mac Apple Silicon (arm64) และ Windows x64 แยกกัน ตรวจชื่อไฟล์ให้ตรงระบบก่อนดาวน์โหลด การอัปเดตรุ่นไทยใช้ดาวน์โหลดจาก Releases โดยตรง

## LightCraft TH 0.20.0-th.1

[ดาวน์โหลด lightcraft-0.20.0-th.1-windows-x64.msi](https://github.com/tapanapon-com/lightcraft-th/releases/download/v0.20.0-th.1/lightcraft-0.20.0-th.1-windows-x64.msi) · [ไฟล์อื่นและ SHA-256](https://github.com/tapanapon-com/lightcraft-th/releases/tag/v0.20.0-th.1) · [วิธีติดตั้งภาษาไทยและภาพหน้าจอ](https://tapanapon.com/blog/lightcraft-th-thai-raw-photo-editor)

## English

Use the MSI for installation or extract the complete portable ZIP before launching the app. Select the correct architecture and compare the matching file's SHA-256 from the same release. Source and symbol archives are not ordinary installers.
