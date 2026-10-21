---
offset: "0x004675a0"
module: "WoW/Source"
file: "WoW/Source/WowServices/WowConnection.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004675a0 — `WowConnection_NewSendNodeCopy`

- **Адрес (Offset):** `0x004675a0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/WowServices/WowConnection.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004675a0
WowConnection::SENDNODE* WowConnection::NewSendNodeCopy(const WowConnection::SENDNODE* source, int32_t size) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004675a0 в IDA Pro / Ghidra
