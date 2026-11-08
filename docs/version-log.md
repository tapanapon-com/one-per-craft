# Version Log / บันทึกรุ่นต้นฉบับ

ตรวจข้อมูล 08/11/2026 21:15 ICT · เป็น snapshot ของ GitHub Releases ไม่ใช่การอัปเดตอัตโนมัติ

ต้นฉบับกับรุ่นไทยมีเวอร์ชันและผลทดสอบแยกกัน รุ่นไทยที่เผยแพร่มี 3 แอป อีก 13 repo ยังเป็นเอกสาร/manifest เท่านั้น

## PhotoCraft — v0.21.0

[Release Notes ต้นฉบับ](https://github.com/storytold/photocraft/releases/tag/v0.21.0) · เผยแพร่ 2026-11-06T20:22:03Z UTC

- เพิ่มตัวเลือกเก็บภาพรวมเอกสารแบบเต็มขนาดไว้ในไฟล์ .pcraft — [ต้นทาง](https://github.com/storytold/photocraft/pull/9913)
- ปรับขั้นตอนบันทึกเพื่อลดการเก็บข้อมูลไฟล์ซ้ำในหน่วยความจำ — [ต้นทาง](https://github.com/storytold/photocraft/pull/8115)
- ปรับการนำเข้า PSD/PSB และ EXR ให้ประมวลผลเป็นช่วงที่จำกัดขนาด — [ต้นทาง](https://github.com/storytold/photocraft/pull/5331)

### ประวัติรุ่นที่ตรวจ

- [v0.21.0](https://github.com/storytold/photocraft/releases/tag/v0.21.0) — 2026-11-06T20:22:03Z
- [v0.20.2](https://github.com/storytold/photocraft/releases/tag/v0.20.2) — 2026-11-05T01:48:22Z
- [v0.20.1](https://github.com/storytold/photocraft/releases/tag/v0.20.1) — 2026-11-03T01:24:40Z

รุ่นไทยที่เผยแพร่: 0.21.0-th.1 · [GitHub รุ่นไทย](https://github.com/tapanapon-com/photocraft-th) · [Version Log รุ่นไทย](https://github.com/tapanapon-com/photocraft-th/blob/main/docs/version-log.md)

รวม tag ต้นฉบับ v0.21.0 ที่ `efb7ebd0c0dab1fc108ee4642aa47c22694271a8`; คำแปลไทย 4,726 รายการ. ตรวจ Mac จาก DMG จริง: ภาษาไทย บันทึก–เปิดไฟล์งาน และภาพผลลัพธ์ผ่าน; MCP 26 เครื่องมือ. Windows x64 ผ่าน native build/CLI/MCP (26 เครื่องมือ), โครงสร้างแพ็กเกจและ SHA-256; ยังไม่ได้ทดสอบทุก workflow ผ่านหน้าจอ Windows [ผลตรวจและ hashes](https://github.com/tapanapon-com/photocraft-th/blob/main/docs/validation-0.21.0-th.1.json)

## VectorCraft — v0.22.0

[Release Notes ต้นฉบับ](https://github.com/storytold/vectorcraft/releases/tag/v0.22.0) · เผยแพร่ 2026-11-06T20:22:17Z UTC

- เลือกความละเอียดของพิกัดพาธเมื่อบันทึกไฟล์งานได้ — [ต้นทาง](https://github.com/storytold/vectorcraft/pull/3990)
- แก้การเปิดไฟล์ EPS ที่สร้างด้วย Ghostscript eps2write — [ต้นทาง](https://github.com/storytold/vectorcraft/pull/5314)
- ปรับ PDF export ให้หมึกสีพิเศษที่ชื่อ All หรือ None คงเป็น spot ink — [ต้นทาง](https://github.com/storytold/vectorcraft/pull/5250)

### ประวัติรุ่นที่ตรวจ

- [v0.22.0](https://github.com/storytold/vectorcraft/releases/tag/v0.22.0) — 2026-11-06T20:22:17Z
- [v0.21.1](https://github.com/storytold/vectorcraft/releases/tag/v0.21.1) — 2026-11-05T02:06:59Z
- [v0.21.0](https://github.com/storytold/vectorcraft/releases/tag/v0.21.0) — 2026-11-03T01:14:20Z

รุ่นไทยที่เผยแพร่: 0.22.0-th.1 · [GitHub รุ่นไทย](https://github.com/tapanapon-com/vectorcraft-th) · [Version Log รุ่นไทย](https://github.com/tapanapon-com/vectorcraft-th/blob/main/docs/version-log.md)

รวม tag ต้นฉบับ v0.22.0 ที่ `654749c16eb20b6d3182a96defb66e11d1a9649a`; คำแปลไทย 7,920 รายการ. ตรวจ Mac จาก DMG จริง: ภาษาไทย บันทึก–เปิดไฟล์งาน และภาพผลลัพธ์ผ่าน; MCP 33 เครื่องมือ. Windows x64 ผ่าน native build/CLI/MCP (33 เครื่องมือ), โครงสร้างแพ็กเกจและ SHA-256; ยังไม่ได้ทดสอบทุก workflow ผ่านหน้าจอ Windows [ผลตรวจและ hashes](https://github.com/tapanapon-com/vectorcraft-th/blob/main/docs/validation-0.22.0-th.1.json)

## FilmCraft — v0.18.0

[Release Notes ต้นฉบับ](https://github.com/storytold/filmcraft/releases/tag/v0.18.0) · เผยแพร่ 2026-11-06T20:21:40Z UTC

- ปรับข้อมูล composition ระดับบนใน AAF ให้มี Usage_TopLevel ตามที่ลงทะเบียนไว้ — [ต้นทาง](https://github.com/storytold/filmcraft/pull/3987)
- แก้การจัดการเครื่องหมาย < ที่ไม่ปิดในข้อความคำบรรยาย TTML — [ต้นทาง](https://github.com/storytold/filmcraft/pull/4105)
- ตรวจช่วงข้อมูล sample ใน MP4 ก่อนจองหน่วยความจำบนเว็บ — [ต้นทาง](https://github.com/storytold/filmcraft/pull/4102)

### ประวัติรุ่นที่ตรวจ

- [v0.18.0](https://github.com/storytold/filmcraft/releases/tag/v0.18.0) — 2026-11-06T20:21:40Z
- [v0.17.1](https://github.com/storytold/filmcraft/releases/tag/v0.17.1) — 2026-11-05T01:47:53Z
- [v0.17.0](https://github.com/storytold/filmcraft/releases/tag/v0.17.0) — 2026-11-03T00:53:23Z

รุ่นไทยที่เผยแพร่: 0.18.0-th.1 · [GitHub รุ่นไทย](https://github.com/tapanapon-com/filmcraft-th) · [Version Log รุ่นไทย](https://github.com/tapanapon-com/filmcraft-th/blob/main/docs/version-log.md)

รวม tag ต้นฉบับ v0.18.0 ที่ `015d5b3ea37e1202a529e6245d3cc021c8c16ffd`; คำแปลไทย 3,786 รายการ. ตรวจ Mac จาก DMG จริง: ภาษาไทย บันทึก–เปิดไฟล์งาน และภาพผลลัพธ์ผ่าน; MCP 17 เครื่องมือ. Windows x64 ผ่าน native build/CLI/MCP (17 เครื่องมือ), โครงสร้างแพ็กเกจและ SHA-256; ยังไม่ได้ทดสอบทุก workflow ผ่านหน้าจอ Windows [ผลตรวจและ hashes](https://github.com/tapanapon-com/filmcraft-th/blob/main/docs/validation-0.18.0-th.1.json)

## LightCraft — v0.19.0

[Release Notes ต้นฉบับ](https://github.com/storytold/lightcraft/releases/tag/v0.19.0) · เผยแพร่ 2026-11-06T20:21:50Z UTC

- ใช้ไลบรารี craftlib สำหรับการอ่านไฟล์ CRW — [ต้นทาง](https://github.com/storytold/lightcraft/pull/3503)
- แก้การเลือกโปรไฟล์เลนส์เมื่อต่อ teleconverter ไม่ให้ใช้โปรไฟล์ของเลนส์เดี่ยวผิดชุด — [ต้นทาง](https://github.com/storytold/lightcraft/pull/3660)
- ปรับการครอปหลังแก้ความคลาดเลนส์ให้อยู่ภายในภาพที่แก้แล้ว — [ต้นทาง](https://github.com/storytold/lightcraft/pull/3012)

### ประวัติรุ่นที่ตรวจ

- [v0.19.0](https://github.com/storytold/lightcraft/releases/tag/v0.19.0) — 2026-11-06T20:21:50Z
- [v0.18.1](https://github.com/storytold/lightcraft/releases/tag/v0.18.1) — 2026-11-05T01:25:33Z
- [v0.18.0](https://github.com/storytold/lightcraft/releases/tag/v0.18.0) — 2026-11-03T00:54:20Z

รุ่นไทยที่เผยแพร่: ยังไม่มี · [GitHub รุ่นไทย](https://github.com/tapanapon-com/lightcraft-th)

## PdfCraft — v0.19.0

[Release Notes ต้นฉบับ](https://github.com/storytold/pdfcraft/releases/tag/v0.19.0) · เผยแพร่ 2026-11-06T20:21:58Z UTC

- เตรียมเรนเดอร์หน้าที่อยู่ถัดจากตำแหน่งเลื่อนในมุมมองต่อเนื่อง — [ต้นทาง](https://github.com/storytold/pdfcraft/pull/6063)
- ปรับการเลื่อนด้วยล้อเมาส์ให้ต่อเนื่องและรักษาระยะการเลื่อนอย่างละเอียด — [ต้นทาง](https://github.com/storytold/pdfcraft/pull/6031)
- ปรับ Optimize ให้เข้ารหัสภาพ JBIG2 เฉพาะรูปแบบที่ตัวอ่านของแอปรองรับ — [ต้นทาง](https://github.com/storytold/pdfcraft/pull/5511)

### ประวัติรุ่นที่ตรวจ

- [v0.19.0](https://github.com/storytold/pdfcraft/releases/tag/v0.19.0) — 2026-11-06T20:21:58Z
- [v0.18.2](https://github.com/storytold/pdfcraft/releases/tag/v0.18.2) — 2026-11-05T01:47:43Z
- [v0.18.1](https://github.com/storytold/pdfcraft/releases/tag/v0.18.1) — 2026-11-04T03:51:06Z

รุ่นไทยที่เผยแพร่: ยังไม่มี · [GitHub รุ่นไทย](https://github.com/tapanapon-com/pdfcraft-th)

## EffectCraft — v0.22.0

[Release Notes ต้นฉบับ](https://github.com/storytold/effectcraft/releases/tag/v0.22.0) · เผยแพร่ 2026-11-06T20:26:02Z UTC

- เก็บ matte ที่ Freeze ใน Roto Brush ไว้ในเซสชันได้แม้ไม่มีโมเดลนั้น — [ต้นทาง](https://github.com/storytold/effectcraft/pull/2834)
- ปรับการนำเข้า EDL ให้ใช้ source timecode ของแต่ละไฟล์ได้ตรงตำแหน่ง — [ต้นทาง](https://github.com/storytold/effectcraft/pull/2835)
- กำหนดโปรไฟล์ Rec. 2100 ให้การนำเข้าวิดีโอ BT.2020 PQ และ HLG — [ต้นทาง](https://github.com/storytold/effectcraft/pull/2852)

### ประวัติรุ่นที่ตรวจ

- [v0.22.0](https://github.com/storytold/effectcraft/releases/tag/v0.22.0) — 2026-11-06T20:26:02Z
- [v0.21.1](https://github.com/storytold/effectcraft/releases/tag/v0.21.1) — 2026-11-05T01:47:58Z
- [v0.21.0](https://github.com/storytold/effectcraft/releases/tag/v0.21.0) — 2026-11-03T01:05:56Z

รุ่นไทยที่เผยแพร่: ยังไม่มี · [GitHub รุ่นไทย](https://github.com/tapanapon-com/effectcraft-th)

## DesignCraft — v0.18.0

[Release Notes ต้นฉบับ](https://github.com/storytold/designcraft/releases/tag/v0.18.0) · เผยแพร่ 2026-11-06T20:21:31Z UTC

- เพิ่มงาน parent pages และ alternate layouts พร้อมส่งออกหรือพิมพ์แต่ละ layout/version — [ต้นทาง](https://github.com/storytold/designcraft/pull/1342)
- แก้การคัดลอกกรอบที่มีกรอบข้อความยึดอยู่ให้คงเนื้อหาข้อความไว้ — [ต้นทาง](https://github.com/storytold/designcraft/pull/2348)
- ปรับตารางเครดิตใน About ให้พอดีหน้าต่างและปรับขนาดคอลัมน์ได้ — [ต้นทาง](https://github.com/storytold/designcraft/pull/2264)

### ประวัติรุ่นที่ตรวจ

- [v0.18.0](https://github.com/storytold/designcraft/releases/tag/v0.18.0) — 2026-11-06T20:21:31Z
- [v0.17.2](https://github.com/storytold/designcraft/releases/tag/v0.17.2) — 2026-11-05T01:47:37Z
- [v0.17.1](https://github.com/storytold/designcraft/releases/tag/v0.17.1) — 2026-11-04T20:37:45Z

รุ่นไทยที่เผยแพร่: ยังไม่มี · [GitHub รุ่นไทย](https://github.com/tapanapon-com/designcraft-th)

## FigCraft — v0.16.0

[Release Notes ต้นฉบับ](https://github.com/storytold/figcraft/releases/tag/v0.16.0) · เผยแพร่ 2026-11-06T20:21:35Z UTC

- ปรับการประมวลผลข้อมูล keyed-list ในงานร่วมกันให้ใช้ดัชนีภายใน batch — [ต้นทาง](https://github.com/storytold/figcraft/pull/1893)
- แจ้งปฏิเสธรูปแบบเส้นประที่ไม่ถูกต้อง แทนการทิ้งค่าบางส่วนเงียบ ๆ — [ต้นทาง](https://github.com/storytold/figcraft/pull/1899)
- แก้การคงระยะกวาดของวงรีในไฟล์ .fig เมื่อมุมเริ่มต้นหมุนหลายรอบ — [ต้นทาง](https://github.com/storytold/figcraft/pull/1891)

### ประวัติรุ่นที่ตรวจ

- [v0.16.0](https://github.com/storytold/figcraft/releases/tag/v0.16.0) — 2026-11-06T20:21:35Z
- [v0.15.1](https://github.com/storytold/figcraft/releases/tag/v0.15.1) — 2026-11-05T01:48:05Z
- [v0.15.0](https://github.com/storytold/figcraft/releases/tag/v0.15.0) — 2026-11-03T00:56:47Z

รุ่นไทยที่เผยแพร่: ยังไม่มี · [GitHub รุ่นไทย](https://github.com/tapanapon-com/figcraft-th)

## TextureCraft — v0.4.0

[Release Notes ต้นฉบับ](https://github.com/storytold/texturecraft/releases/tag/v0.4.0) · เผยแพร่ 2026-11-06T20:22:12Z UTC

- กู้เปิดโปรเจกต์เก่าที่ใช้ค่า bake settings ซึ่งเข้ากับรุ่นปัจจุบันไม่ได้ — [ต้นทาง](https://github.com/storytold/texturecraft/pull/248)
- เพิ่มรายการ mesh map bakers และการตั้งค่าแยกแต่ละ map ในโหมด Bake — [ต้นทาง](https://github.com/storytold/texturecraft/pull/257)
- เพิ่ม camera bookmarks ด้วย Ctrl+1…9 พร้อมการเคลื่อนมุมมองอย่างต่อเนื่อง — [ต้นทาง](https://github.com/storytold/texturecraft/pull/260)

### ประวัติรุ่นที่ตรวจ

- [v0.4.0](https://github.com/storytold/texturecraft/releases/tag/v0.4.0) — 2026-11-06T20:22:12Z
- [v0.3.2](https://github.com/storytold/texturecraft/releases/tag/v0.3.2) — 2026-11-05T01:24:44Z
- [v0.3.1](https://github.com/storytold/texturecraft/releases/tag/v0.3.1) — 2026-11-04T18:09:10Z

รุ่นไทยที่เผยแพร่: ยังไม่มี · [GitHub รุ่นไทย](https://github.com/tapanapon-com/texturecraft-th)

## MaterialCraft — v0.2.0

[Release Notes ต้นฉบับ](https://github.com/storytold/materialcraft/releases/tag/v0.2.0) · เผยแพร่ 2026-11-06T20:21:54Z UTC

- รองรับความโปร่งใสในมุมมอง 3 มิติ และเพิ่มการเลือก ลบ สลับ และจัดเส้นเชื่อมใหม่ — [ต้นทาง](https://github.com/storytold/materialcraft/pull/36)
- เพิ่ม histogram editor พร้อมตัวจับช่วงค่าใน Levels — [ต้นทาง](https://github.com/storytold/materialcraft/pull/37)
- เพิ่ม Export outputs ในเมนูคลิกขวาของกราฟใน explorer — [ต้นทาง](https://github.com/storytold/materialcraft/pull/25)

### ประวัติรุ่นที่ตรวจ

- [v0.2.0](https://github.com/storytold/materialcraft/releases/tag/v0.2.0) — 2026-11-06T20:21:54Z
- [v0.1.2](https://github.com/storytold/materialcraft/releases/tag/v0.1.2) — 2026-11-05T01:24:43Z
- [v0.1.1](https://github.com/storytold/materialcraft/releases/tag/v0.1.1) — 2026-11-04T18:08:56Z

รุ่นไทยที่เผยแพร่: ยังไม่มี · [GitHub รุ่นไทย](https://github.com/tapanapon-com/materialcraft-th)

## WordCraft — v0.16.0

[Release Notes ต้นฉบับ](https://github.com/storytold/wordcraft/releases/tag/v0.16.0) · เผยแพร่ 2026-11-06T20:22:22Z UTC

- แก้การคลิกในกล่องข้อความให้เข้าตัวอักษร แทนภาพที่อยู่ข้างใต้ — [ต้นทาง](https://github.com/storytold/wordcraft/pull/4240)
- แสดงว่าฟอนต์ที่เอกสารใช้อยู่ตัวใดยังไม่ได้ติดตั้งในเครื่อง — [ต้นทาง](https://github.com/storytold/wordcraft/pull/4770)
- ปรับการอ่าน DOCX ให้ shading แบบ nil ไม่ลงสี และใช้สีกรอบจาก theme ตามที่กำหนด — [ต้นทาง](https://github.com/storytold/wordcraft/pull/4705)

### ประวัติรุ่นที่ตรวจ

- [v0.16.0](https://github.com/storytold/wordcraft/releases/tag/v0.16.0) — 2026-11-06T20:22:22Z
- [v0.15.2](https://github.com/storytold/wordcraft/releases/tag/v0.15.2) — 2026-11-05T01:34:30Z
- [v0.15.1](https://github.com/storytold/wordcraft/releases/tag/v0.15.1) — 2026-11-04T03:51:07Z

รุ่นไทยที่เผยแพร่: ยังไม่มี · [GitHub รุ่นไทย](https://github.com/tapanapon-com/wordcraft-th)

## SoundCraft — v0.18.0

[Release Notes ต้นฉบับ](https://github.com/storytold/soundcraft/releases/tag/v0.18.0) · เผยแพร่ 2026-11-06T20:22:08Z UTC

- ปรับการตรวจ controller MIDI ซ้ำโดยแยกตาม channel และชนิด — [ต้นทาง](https://github.com/storytold/soundcraft/pull/1298)
- ปรับการจับคู่ automation lanes กับพารามิเตอร์ของ insert ใน Mixer — [ต้นทาง](https://github.com/storytold/soundcraft/pull/1299)
- รักษา bext chunk ของไฟล์ต้นทาง BWF ระหว่างการแปลงไฟล์ — [ต้นทาง](https://github.com/storytold/soundcraft/pull/1314)

### ประวัติรุ่นที่ตรวจ

- [v0.18.0](https://github.com/storytold/soundcraft/releases/tag/v0.18.0) — 2026-11-06T20:22:08Z
- [v0.17.1](https://github.com/storytold/soundcraft/releases/tag/v0.17.1) — 2026-11-05T01:24:46Z
- [v0.17.0](https://github.com/storytold/soundcraft/releases/tag/v0.17.0) — 2026-11-03T00:44:42Z

รุ่นไทยที่เผยแพร่: ยังไม่มี · [GitHub รุ่นไทย](https://github.com/tapanapon-com/soundcraft-th)

## DeckCraft — v0.16.0

[Release Notes ต้นฉบับ](https://github.com/storytold/deckcraft/releases/tag/v0.16.0) · เผยแพร่ 2026-11-06T20:21:27Z UTC

- ปุ่ม Preview ของ transition เริ่มเล่นตัวอย่างจากสไลด์ก่อนหน้า — [ต้นทาง](https://github.com/storytold/deckcraft/pull/1679)
- รักษาขนาด bullet ที่ผู้สร้างกำหนดเป็นหน่วย points — [ต้นทาง](https://github.com/storytold/deckcraft/pull/1588)
- เพิ่มป้ายชื่อให้ตัวเลือกของเอฟเฟกต์แอนิเมชัน — [ต้นทาง](https://github.com/storytold/deckcraft/pull/1579)

### ประวัติรุ่นที่ตรวจ

- [v0.16.0](https://github.com/storytold/deckcraft/releases/tag/v0.16.0) — 2026-11-06T20:21:27Z
- [v0.15.1](https://github.com/storytold/deckcraft/releases/tag/v0.15.1) — 2026-11-05T01:24:47Z
- [v0.15.0](https://github.com/storytold/deckcraft/releases/tag/v0.15.0) — 2026-11-03T00:51:03Z

รุ่นไทยที่เผยแพร่: ยังไม่มี · [GitHub รุ่นไทย](https://github.com/tapanapon-com/deckcraft-th)

## CADCraft — v0.18.0

[Release Notes ต้นฉบับ](https://github.com/storytold/cadcraft/releases/tag/v0.18.0) · เผยแพร่ 2026-11-06T20:21:13Z UTC

- แสดงเมื่อ Autosave ล้มเหลว และกู้งานหลังแอปขัดข้องในการเปิดครั้งแรก — [ต้นทาง](https://github.com/storytold/cadcraft/pull/2670)
- เมื่อส่วนติดต่อเกิด panic ให้บันทึกงานและรายงานเหตุการณ์ — [ต้นทาง](https://github.com/storytold/cadcraft/pull/2671)
- แยกการอ่านและเขียน DWG ไปทำงานในโปรเซสลูก — [ต้นทาง](https://github.com/storytold/cadcraft/pull/2673)

### ประวัติรุ่นที่ตรวจ

- [v0.18.0](https://github.com/storytold/cadcraft/releases/tag/v0.18.0) — 2026-11-06T20:21:13Z
- [v0.17.1](https://github.com/storytold/cadcraft/releases/tag/v0.17.1) — 2026-11-05T01:24:49Z
- [v0.17.0](https://github.com/storytold/cadcraft/releases/tag/v0.17.0) — 2026-11-03T00:54:01Z

รุ่นไทยที่เผยแพร่: ยังไม่มี · [GitHub รุ่นไทย](https://github.com/tapanapon-com/cadcraft-th)

## GridCraft — v0.17.0

[Release Notes ต้นฉบับ](https://github.com/storytold/gridcraft/releases/tag/v0.17.0) · เผยแพร่ 2026-11-06T20:21:45Z UTC

- ปรับจุดอ้างอิงสูตรสัมพัทธ์ใน Data Validation และ Conditional Formatting ให้เริ่มจากเซลล์ซ้ายบนของทุกช่วง — [ต้นทาง](https://github.com/storytold/gridcraft/pull/3173)
- ตรวจสิทธิ์ของชีตที่ย้ายคอลัมน์ และปฏิเสธการแก้ไขที่ปลดล็อกเซลล์ซึ่งถูกป้องกัน — [ต้นทาง](https://github.com/storytold/gridcraft/pull/3196)
- ปรับการเปลี่ยนชื่อหัวตารางซ้ำใน XLSX เพื่อลดการลอง suffix ที่ถูกใช้แล้ว — [ต้นทาง](https://github.com/storytold/gridcraft/pull/3213)

### ประวัติรุ่นที่ตรวจ

- [v0.17.0](https://github.com/storytold/gridcraft/releases/tag/v0.17.0) — 2026-11-06T20:21:45Z
- [v0.16.1](https://github.com/storytold/gridcraft/releases/tag/v0.16.1) — 2026-11-05T01:24:51Z
- [v0.16.0](https://github.com/storytold/gridcraft/releases/tag/v0.16.0) — 2026-11-03T00:45:51Z

รุ่นไทยที่เผยแพร่: ยังไม่มี · [GitHub รุ่นไทย](https://github.com/tapanapon-com/gridcraft-th)

## Craft Anything — v0.5.0

[Release Notes ต้นฉบับ](https://github.com/storytold/craft-anything/releases/tag/v0.5.0) · เผยแพร่ 2026-11-06T20:21:17Z UTC

- ให้ OpenCode ที่รันแบบ native ใช้เครื่องมือ Craft Anything และแสดงการเรียกเครื่องมือได้ — [ต้นทาง](https://github.com/storytold/craft-anything/pull/800)
- ปรับช่องพิมพ์คำสั่งใน Advanced console ให้เริ่มต้นที่สามบรรทัด — [ต้นทาง](https://github.com/storytold/craft-anything/pull/979)
- แก้การจัดประเภทไม่ให้โปรแกรมเล่นวิดีโอหรือเพลงถูกนับเป็นเกม — [ต้นทาง](https://github.com/storytold/craft-anything/pull/970)

### ประวัติรุ่นที่ตรวจ

- [v0.5.0](https://github.com/storytold/craft-anything/releases/tag/v0.5.0) — 2026-11-06T20:21:17Z
- [v0.4.0](https://github.com/storytold/craft-anything/releases/tag/v0.4.0) — 2026-11-06T04:08:45Z
- [v0.3.0](https://github.com/storytold/craft-anything/releases/tag/v0.3.0) — 2026-11-02T17:58:25Z

รุ่นไทยที่เผยแพร่: ยังไม่มี · [GitHub รุ่นไทย](https://github.com/tapanapon-com/craft-anything-th)
