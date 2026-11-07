# เชื่อม Craft กับ Codex / Claude ผ่าน MCP

อ่าน [คู่มือรวมที่มีตัวอย่าง Mac และ Windows](https://tapanapon.com/blog/one-per-craft-connect-codex-claude-mcp) และเอกสาร MCP ของแอปที่ต้องการก่อนตั้งค่า

1. ติดตั้งตัว CLI ของแอปและตรวจ absolute path ด้วย `--help` / `mcp --help`
2. ลงทะเบียนพาธและ arguments กับ Codex, Claude Code หรือ Claude Desktop ตามคู่มือ
3. เลือก headless หากต้องการทำงานโดยไม่เปิดหน้าต่าง หรือใช้ live/bridge/connect/attach ที่แอปนั้นรองรับเพื่อเห็นงานใน GUI
4. พอร์ต token และ file-root flags ต่างกันในแต่ละแอป อย่านำ flags ของแอปหนึ่งไปใช้กับอีกตัวโดยไม่ตรวจ

โหมด headless ไม่เปลี่ยนงานในหน้าต่าง GUI ที่เปิดค้างโดยอัตโนมัติ การมี app repository หรือ source ZIP ไม่ได้ติดตั้ง CLI/MCP ให้เครื่องของผู้ใช้

คู่มือเดิมมีผลทดสอบ MCP initialize/tools-list ของ VectorCraft และ PhotoCraft บน Mac ส่วนแอปอื่นอ้างอิงเอกสารต้นทาง ไม่อ้างว่าได้ทดสอบ runtime รุ่นไทยครบ 16 แอปแล้ว

## English

Install the matching CLI, verify its absolute path and register its app-specific stdio MCP command. Headless and live GUI sessions differ, and bridge/connect/attach/root/token flags are not interchangeable. Use the linked guide and each app's upstream documentation; repository creation is not runtime validation.
