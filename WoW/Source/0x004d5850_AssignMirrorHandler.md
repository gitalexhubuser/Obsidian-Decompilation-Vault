---
offset: "0x004d5850"
module: "WoW/Source"
file: "WoW/Source/ObjectMgrClient/ObjectMgrClient.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004d5850 — `AssignMirrorHandler`

- **Адрес (Offset):** `0x004d5850`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/ObjectMgrClient/ObjectMgrClient.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004d5850
static CMirrorHandler* AssignMirrorHandler(TSList<CMirrorHandler, TSGetLink<CMirrorHandler> >* list, uint32_t fieldByteOffset, uint32_t mirrorByteOffset, uint32_t fieldByteSize, MIRRORHANDLERFUNC function, void* param, HANDLER_PRIORITY priority, int32_t alwaysFire) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004d5850 в IDA Pro / Ghidra
