---
offset: "0x00467540"
module: "WoW/Source"
file: "WoW/Source/WowServices/WowConnection.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00467540 — `WowConnection_NewSendNodePacket`

- **Адрес (Offset):** `0x00467540`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/WowConnection.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00467540
WowConnection::SENDNODE* WowConnection::NewSendNodePacket(const void* data, int32_t size, bool raw) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00467540 в IDA Pro / Ghidra
