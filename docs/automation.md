# เชื่อม Craft กับ Codex / Claude ผ่าน MCP

อ่าน [คู่มือรวมที่มีตัวอย่าง Mac และ Windows](https://tapanapon.com/blog/one-per-craft-connect-codex-claude-mcp) และเอกสาร MCP ของแอปที่ต้องการก่อนตั้งค่า

1. ติดตั้งตัว CLI ของแอปและตรวจ absolute path ด้วย `--help` / `mcp --help`
2. ลงทะเบียนพาธและ arguments กับ Codex, Claude Code หรือ Claude Desktop ตามคู่มือ
3. เลือก headless หากต้องการทำงานโดยไม่เปิดหน้าต่าง หรือใช้ live/bridge/connect/attach ที่แอปนั้นรองรับเพื่อเห็นงานใน GUI
4. พอร์ต token และ file-root flags ต่างกันในแต่ละแอป อย่านำ flags ของแอปหนึ่งไปใช้กับอีกตัวโดยไม่ตรวจ

โหมด headless ไม่เปลี่ยนงานในหน้าต่าง GUI ที่เปิดค้างโดยอัตโนมัติ การมี app repository หรือ source ZIP ไม่ได้ติดตั้ง CLI/MCP ให้เครื่องของผู้ใช้

ทั้ง 3 รุ่นไทยผ่าน MCP initialize/tools-list จาก CLI ในแพ็กเกจ Mac ที่ mount จริง และจาก Windows x64 CI ส่วนอีก 13 แอปอ้างอิงเอกสารต้นทาง ยังไม่ใช่แอปไทยที่ทดสอบ runtime แล้ว

## CLI ที่แนบในแพ็กเกจ Mac

| แอป | รุ่นไทย | พาธ CLI หลังลากแอปเข้า Applications |
| --- | --- | --- |
| PhotoCraft | 0.21.0-th.1 | `/Applications/PhotoCraft.app/Contents/MacOS/photocraft-cli` |
| VectorCraft | 0.22.0-th.1 | `/Applications/VectorCraft.app/Contents/MacOS/vectorcraft-cli` |
| FilmCraft | 0.18.0-th.1 | `/Applications/FilmCraft.app/Contents/MacOS/filmcraft-cli` |

Windows MSI/portable รวม `<app>-cli.exe` ข้าง GUI ให้ใช้พาธติดตั้งจริง ไม่ใช้พาธ Mac บน Windows อ่าน flags ของแต่ละแอปจากคู่มือรวมก่อนลงทะเบียน โดยเฉพาะ VectorCraft ที่ต้องกำหนดโฟลเดอร์อ่านและเขียนให้มีอยู่จริง

## English

Install the matching CLI, verify its absolute path and register its app-specific stdio MCP command. Headless and live GUI sessions differ, and bridge/connect/attach/root/token flags are not interchangeable. Use the linked guide and each app's upstream documentation; repository creation is not runtime validation.
