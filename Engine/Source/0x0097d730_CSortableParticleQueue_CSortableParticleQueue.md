---
offset: "0x0097d730"
module: "Engine/Source"
file: "Engine/Source/Services/ParticleSystem2.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0097d730 — `CSortableParticleQueue_CSortableParticleQueue`

- **Адрес (Offset):** `0x0097d730`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Services/ParticleSystem2.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0097d730
CSortableParticleQueue::CSortableParticleQueue(const uint32_t* params) : CMemBlock(sizeof(CSortableParticleRecord) * params[0], 0, typeid(CSortableParticleRecord).raw_name(), SLOG_OBJECT) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0097d730 в IDA Pro / Ghidra
