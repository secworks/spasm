// This is a first, simple test program.

.define screen = 0x0400

.addr = 0x1000
                ldy #$01
:l1             tya
                sta screen,y
                iny
                bne l1
                rts
