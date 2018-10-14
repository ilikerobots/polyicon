PROJECT     := $(notdir ${PWD})
FONT_NAME   := linearicons


################################################################################
## ! DO NOT EDIT BELOW THIS LINE, UNLESS YOU REALLY KNOW WHAT ARE YOU DOING ! ##
################################################################################


TMP_PATH    := /tmp/${PROJECT}-$(shell date +%s)
REMOTE_NAME ?= origin
REMOTE_REPO ?= $(shell git config --get remote.${REMOTE_NAME}.url)


PWD  := $(shell pwd)
BIN  := ./node_modules/.bin


dump:
	rm -rf ./src/svg/
	mkdir ./src/svg/
	${BIN}/svg-font-dump -n -c `pwd`/config.yml -f -i ./src/original/linearicons.svg -o ./src/svg/ -d diff.yml
	${BIN}/svgo --config `pwd`/dump.svgo.yml -f ./src/svg




dist: font html

font:
	@if test ! -d node_modules ; then \
		echo "dependencies not found:" >&2 ; \
		echo "  make dependencies" >&2 ; \
		exit 128 ; \
		fi

	${BIN}/svg-font-create -c config.yml -i ./src/svg -o "./font/$(FONT_NAME).svg"
	fontforge -c 'import fontforge; font = fontforge.open("./font/$(FONT_NAME).svg"); font.generate("./font/$(FONT_NAME).ttf")'

	@if test `which ttfautohint` ; then \
		ttfautohint --latin-fallback --hinting-limit=200 --hinting-range-max=50 --symbol ./font/$(FONT_NAME).ttf ./font/$(FONT_NAME)-hinted.ttf && \
		mv ./font/$(FONT_NAME)-hinted.ttf ./font/$(FONT_NAME).ttf ; \
		else \
		echo "WARNING: ttfautohint not found. Font will not be hinted." >&2 ; \
		fi

	${BIN}/ttf2eot "./font/$(FONT_NAME).ttf" "./font/$(FONT_NAME).eot"
	${BIN}/ttf2woff "./font/$(FONT_NAME).ttf" "./font/$(FONT_NAME).woff"


html:
	@${BIN}/jade -O '$(shell node_modules/.bin/js-yaml -j config.yml)' ./src/demo/demo.jade -o ./font


gh-pages:
	@if test -z ${REMOTE_REPO} ; then \
		echo 'Remote repo URL not found' >&2 ; \
		exit 128 ; \
		fi
	cp -r ./font ${TMP_PATH} && \
		touch ${TMP_PATH}/.nojekyll
	cd ${TMP_PATH} && \
		git init && \
		git add . && \
		git commit -q -m 'refreshed gh-pages'
	cd ${TMP_PATH} && \
		git remote add remote ${REMOTE_REPO} && \
		git push --force remote +master:gh-pages
	rm -rf ${TMP_PATH}


dependencies:
	@if test ! `which npm` ; then \
		echo "Node.JS and NPM are required for html demo generation." >&2 ; \
		echo "This is non-fatal error and you'll still be able to build font," >&2 ; \
		echo "however, to build demo with >> make html << you need:" >&2 ; \
		echo "  - Install Node.JS and NPM" >&2 ; \
		echo "  - Run this task once again" >&2 ; \
		exit 128 ; \
		fi
	@if test ! `which ttfautohint` ; then \
		echo "Trying to install ttf-autohint from repository..." ; \
		apt-cache policy -q=2 | grep -q 'Candidate' && \
			sudo apt-get install ttfautohint && \
			echo "SUCCESS" || echo "FAILED" ; \
		fi
	@if test ! `which ttfautohint` ; then \
		echo "Trying to install ttf-autohint from Debian's repository..." ; \
		curl --silent --show-error --output /tmp/ttfautohint.deb \
			http://ftp.de.debian.org/debian/pool/main/t/ttfautohint/ttfautohint_0.95-1_amd64.deb && \
		sudo dpkg -i /tmp/ttfautohint.deb && \
			echo "SUCCESS" || echo "FAILED" ; \
		fi
	@if test ! -d node_modules ; then \
		npm install ; \
		fi

.PHONY: font html dist dump gh-pages dependencies
