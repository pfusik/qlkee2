run: qlkee2.xex
	start $<

qlkee2.xex: qlkee2.asx qlka.asx
	xasm -o $@ $<

qlka.asx: png2gr9.py qlka.png
	python $^ >$@

qlkee2.zip: qlkee2.xex qlkee2.txt
	7z a -mx=9 -bd -bso0 -tzip $@ $^

clean:
	$(RM) qlkee2.xex qlka.asx
