---
offset: "0x006b1b80"
module: "WoW/Source"
file: "WoW/Source/WowServices/WowConnection.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x006b1b80 — `WowConnectionResponse_WCDataReady`

- **Адрес (Offset):** `0x006b1b80`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/WowConnection.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x006b1b80
void WowConnectionResponse::WCDataReady(WowConnection* connection, uint32_t timeStamp, uint8_t* data, int32_t length) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x006b1b80 в IDA Pro / Ghidra
