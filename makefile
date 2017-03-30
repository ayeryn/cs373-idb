FILES :=                              \
    apiary.apib                       \
    IDB1.log                          \
    models.html                       \
    app/models.py                     \
    app/tests.py                      \
    UML.pdf                           \

check:
	@not_found=0;                                 \
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
    echo "success";

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -rf __pycache__

config:
	git config -l

format:
	$(AUTOPEP8) -i app/tests.py

scrub:
	make clean
	rm -f IDB1.log

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

test: check

log:
	git log > IDB1.log
