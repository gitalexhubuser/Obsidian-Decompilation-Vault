---
offset: "0x0095e6e0"
module: "Engine/Source"
file: "Engine/Source/Frame/CSimpleMovieFrame.cpp"
tags:
  - wowdecomp
  - offset
  - module/engine_source
---

# 0x0095e6e0 — `CSimpleMovieFrame_CSimpleMovieFrame`

- **Адрес (Offset):** `0x0095e6e0`
- **Модуль:** `Engine/Source`
- **Файл исходника:** `Engine/Source/Frame/CSimpleMovieFrame.cpp`

## Сигнатура C++
```cpp
// OFFSET: 0x0095e6e0
CSimpleMovieFrame::CSimpleMovieFrame(CSimpleFrame* parent) : CSimpleFrame(parent), m_isPlaying(0), m_finished(0), m_subtitlesEnabled(0), m_audioRestart(0), m_volume(100), m_decoder(0), m_frameBuffer(nullptr), m_videoData(nullptr), m_audioData(nullptr) {
```

## Исследование и заметки
- [ ] Открыть адрес 0x0095e6e0 в IDA Pro / Ghidra
