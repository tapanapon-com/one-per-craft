# ติดตั้งบน Windows / Windows installation

เลือกแอปและรุ่นจาก [README](../README.md) หรือ [เว็บไซต์](https://tapanapon.com/one-per-craft) โดยแยกต้นฉบับจากแพ็กเกจไทย

- **MSI:** ปิดแอปเดิม เปิดตัวติดตั้ง ทำตามหน้าจอ แล้วเปิดผ่าน Start Menu
- **Portable ZIP:** ใช้ Extract All แตกไฟล์ทั้งหมดลงโฟลเดอร์ที่เขียนได้ แล้วเปิด `.exe` ของแอป เก็บไฟล์ประกอบไว้ครบ
- เลือก x64, ARM64 หรือ x86 ให้ตรงกับเครื่องและการรองรับของต้นทาง
- ตรวจ SHA-256 โดยใช้รายการชื่อไฟล์และ Release เดียวกัน ไม่ใช้ hash ของ ZIP มาเทียบ MSI
- Source code ZIP ไม่ใช่ตัวติดตั้ง; ไฟล์ symbols เป็นข้อมูลสำหรับวิเคราะห์ปัญหา

[คู่มือ MSI/Portable/GitHub ฉบับเต็ม](https://tapanapon.com/blog/one-per-craft-install-windows-github)

## English

Use the MSI for installation or extract the complete portable ZIP before launching the app. Select the correct architecture and compare the matching file's SHA-256 from the same release. Source and symbol archives are not ordinary installers.
