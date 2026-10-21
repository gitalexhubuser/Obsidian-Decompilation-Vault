---
offset: "0x00925e60"
module: "Engine/Source"
file: "Engine/Source/SoundEngine/fmodex/src/fmod_octree.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x00925e60 — `Octree_testLine`

- **Адрес (Offset):** `0x00925e60`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/SoundEngine/fmodex/src/fmod_octree.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x00925e60
bool Octree::testLine(bool (*octreeLineTestCallback)(OctreeNode* item, void* data), void* data, const FMOD_VECTOR& a, const FMOD_VECTOR& b)
```

## Исследование и заметки
- [ ] Открыть адрес 0x00925e60 в IDA Pro / Ghidra
