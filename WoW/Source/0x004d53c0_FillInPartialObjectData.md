---
offset: "0x004d53c0"
module: "WoW/Source"
file: "WoW/Source/ObjectMgrClient/ObjectMgrClient.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004d53c0 — `FillInPartialObjectData`

- **Адрес (Offset):** `0x004d53c0`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/ObjectMgrClient/ObjectMgrClient.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004d53c0
static int32_t FillInPartialObjectData(CGObject_C* object, WOWGUID guid, CDataStore* msg, bool skipMirrorUpdate, bool zeroFillAbsent) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004d53c0 в IDA Pro / Ghidra
