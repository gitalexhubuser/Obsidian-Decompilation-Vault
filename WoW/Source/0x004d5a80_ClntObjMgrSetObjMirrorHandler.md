---
offset: "0x004d5a80"
module: "WoW/Source"
file: "WoW/Source/ObjectMgrClient/ObjectMgrClient.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004d5a80 — `ClntObjMgrSetObjMirrorHandler`

- **Адрес (Offset):** `0x004d5a80`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/ObjectMgrClient/ObjectMgrClient.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004d5a80
void ClntObjMgrSetObjMirrorHandler(WOWGUID guid, OBJECT_TYPE_ID typeId, uint32_t fieldOffset, uint32_t fieldSize, MIRRORHANDLERFUNC function, void* param, HANDLER_PRIORITY priority, int32_t alwaysFire) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004d5a80 в IDA Pro / Ghidra
