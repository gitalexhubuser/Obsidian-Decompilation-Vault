---
offset: "0x0071e400"
module: "WoW/Source"
file: "WoW/Source/Object/ObjectClient/Unit_C.cpp"
tags:
  - wowdecomp
  - offset
  - module/wow_source
---

# 0x0071e400 — `CGUnit_C_ApplyAttachmentAnimOverride`

- **Адрес (Offset):** `0x0071e400`
- **Модуль:** `WoW/Source`
- **Файл исходника:** `WoW/Source/Object/ObjectClient/Unit_C.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0071e400
int32_t CGUnit_C::ApplyAttachmentAnimOverride(const M2BoneSequenceInfo* mount, const M2BoneSequenceInfo* base, const M2BoneSequenceInfo* torso, int32_t hasTorso, M2BoneSequenceInfo* mountOut, M2BoneSequenceInfo* baseOut, M2BoneSequenceInfo* torsoOut, int32_t* keepBase, int32_t* keepTorso) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0071e400 в IDA Pro / Ghidra
