---
offset: "0x00880980"
module: "Engine/Source"
file: "Engine/Source/ComSat/ComSatManager.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00880980 — `Manager_SessionAddRemote`

- **Адрес (Offset):** `0x00880980`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/ComSat/ComSatManager.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00880980
bool ComSat::Manager::SessionAddRemote(uint64_t session, uint64_t talker, uint8_t networkId, const uint8_t (&key)[16], const char* address) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x00880980 в IDA Pro / Ghidra
