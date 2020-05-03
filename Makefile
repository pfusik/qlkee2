run: qlkee2.xex
	start $<

qlkee2.xex: qlkee2.asx qlka.asx
	xasm -o $@ $<

qlka.asx: png2gr9.py qlka.png
	python $^ >$@

clean:
	$(RM) qlkee2.xex qlka.asx
