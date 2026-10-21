---
offset: "0x004d5b40"
module: "WoW/Source"
file: "WoW/Source/ObjectMgrClient/ObjectMgrClient.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x004d5b40 — `ClntObjMgrUnsetObjMirrorHandler`

- **Адрес (Offset):** `0x004d5b40`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/ObjectMgrClient/ObjectMgrClient.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x004d5b40
void ClntObjMgrUnsetObjMirrorHandler(WOWGUID guid, OBJECT_TYPE_ID typeId, uint32_t fieldOffset, MIRRORHANDLERFUNC function, void* param) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x004d5b40 в IDA Pro / Ghidra
