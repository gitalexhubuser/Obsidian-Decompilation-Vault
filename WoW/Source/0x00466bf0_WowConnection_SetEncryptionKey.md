---
offset: "0x00466bf0"
module: "WoW/Source"
file: "WoW/Source/WowServices/WowConnection.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x00466bf0 — `WowConnection_SetEncryptionKey`

- **Адрес (Offset):** `0x00466bf0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/WowConnection.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00466bf0
void WowConnection::SetEncryptionKey(const uint8_t* key, uint8_t keyLength, uint8_t direction, const uint8_t* seed, uint8_t seedLength) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00466bf0 в IDA Pro / Ghidra
