import struct


class CIFF:
    """
    Holds data of a CIFF image
    """

    def __init__(
            self,
            magic_chars="CIFF",
            header_size_long=0,
            content_size_long=0,
            width_long=0,
            height_long=0,
            caption_string="",
            tags_list=None,
            pixels_list=None
    ):
        """
        Constructor for CIFF images

        :param magic_chars: the magic "CIFF" characters
        :param header_size_long: size of the header in bytes (8-byte-long int)
        :param content_size_long: size of content in bytes 8-byte-long int)
        :param width_long: width of the image (8-byte-long int)
        :param height_long: height of the image (8-byte-long int)
        :param caption_string: caption of the image (string)
        :param tags_list: list of tags in the image
        :param pixels_list: list of pixels to display
        """
        self._magic = magic_chars
        self._header_size = header_size_long
        self._content_size = content_size_long
        self._width = width_long
        self._height = height_long
        self._caption = caption_string
        if tags_list is None:
            self._tags = []
        else:
            self._tags = tags_list
        if pixels_list is None:
            self._pixels = []
        else:
            self._pixels = pixels_list
        self._is_valid = True

    #
    # Properties
    #

    @property
    def is_valid(self):
        """
        A flag indicating whether the the CIFF image conforms
        with the specification or not

        :return: boolean
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, value):
        self._is_valid = value

    @property
    def magic(self):
        """
        The parsed magic characters

        :return: str
        """
        return self._magic

    @magic.setter
    def magic(self, value):
        self._magic = value

    @property
    def header_size(self):
        """
        The parsed header size

        :return: int
        """
        return self._header_size

    @header_size.setter
    def header_size(self, value):
        self._header_size = value

    @property
    def content_size(self):
        """
        The parsed content size

        :return: int
        """
        return self._content_size

    @content_size.setter
    def content_size(self, value):
        self._content_size = value

    @property
    def width(self):
        """
        The parsed width of the image

        :return: int
        """
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        """
        The parsed height of the image

        :return: int
        """
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def caption(self):
        """
        The parsed image caption

        :return: str
        """
        return self._caption

    @caption.setter
    def caption(self, value):
        self._caption = value

    @property
    def tags(self):
        """
        The parsed list of tags

        :return: list of strings
        """
        return self._tags

    @tags.setter
    def tags(self, value):
        self._tags = value

    @property
    def pixels(self):
        """
        The parsed pixels

        :return: list
        """
        return self._pixels

    @pixels.setter
    def pixels(self, value):
        self._pixels = value

    #
    # Static methods
    #

    @staticmethod
    def parse_ciff_file(file_path):
        """
        Parses a CIFF file and constructs the corresponding object

        TODO: make sure that malformed input cannot crash the parsing method

        :param file_path: path the to file to be parsed (string)
        :return: the parsed CIFF object
        """
        new_ciff = CIFF()
        bytes_read = 0
        try:
            with open(file_path, "rb") as ciff_file:

                magic = ciff_file.read(4)
                if len(magic) != 4:
                   raise Exception("Magic must contain 4 bytes!")
                bytes_read += 4
                new_ciff.magic = magic.decode('ascii')
                if new_ciff.magic != "CIFF":
                   new_ciff.is_valid = Flase;
                   raise Exception("The magic must be CIFF")

                h_size = ciff_file.read(8)
                if len(h_size) != 8:
                   raise Exception("h_size must contain 8 bytes")
                bytes_read += 8
                new_ciff.header_size = struct.unpack("Q", h_size)[0]
                if new_ciff.header_size < 38 \
                       or new_ciff.header_size > 2**64-1 :
                   raise Exception("Header Size not in Range!")

                c_size = ciff_file.read(8)
                if len(c_size) != 8:
                   raise Exception("Conent header does not contain the right amount of bytes!")
                bytes_read += 8
                new_ciff.content_size = struct.unpack("Q", c_size)[0]

                width = ciff_file.read(8)
                if len(width) != 8:
                   raise Exception("Widht header doen not cotain the right amount of bytes!")
                bytes_read += 8
                new_ciff.width = struct.unpack("Q", width)[0]

                height = ciff_file.read(8)
                if len(height) != 8:
                    raise Exception("Height header doen not cotain the right amount of bytes!")
                bytes_read += 8
                new_ciff.height = struct.unpack("Q", height)[0]
                if new_ciff.content_size != new_ciff.width*new_ciff.height*3:
                    raise Exception("Context size does not match with width and height!")

                caption = ""
                c = ciff_file.read(1)
                if len(c) != 1:
                    raise Exception("Caption should conatin \n")
                bytes_read += 1
                char = c.decode('ascii')
                while char != '\n':
                    caption += char
                    c = ciff_file.read(1)
                    if len(c) != 1:
                        raise Exception("Caption should conatin \n")
                    bytes_read += 1
                    char = c.decode('ascii')
                new_ciff.caption = caption

                tags = list()
                tag = ""
                while bytes_read != new_ciff.header_size:
                    c = ciff_file.read(1)
                    if len(c) != 1:
                        raise Exception("Invalid image")
                    bytes_read += 1
                    char = c.decode('ascii')
                    if char == '\n':
                       raise Exception("Tags contain no \n")
                    tag += char
                    if char == '\0':
                        tags.append(tag)
                        tag = ""
                    if (bytes_read == new_ciff.header_size) and char != '\0':
                       raise Exception("Last byte on tags should be '\0'")
                
                for tag in tags:
                   if tag[-1] != '\0':
                       raise Exception("Tag does not end with '\0'")

                new_ciff.tags = tags
                
                while bytes_read < new_ciff.header_size+new_ciff.content_size:
                    c = ciff_file.read(3)
                    if len(c) != 3:
                        raise Exception("One of the pixels is not 3 bytes!")
                    bytes_read += 3
                    pixel = struct.unpack("BBB", c)
                    new_ciff.pixels.append(pixel)
                
                end = ciff_file.read(1)
                if len(end) == 1:
                    raise Exception("Read the file but not the end of file!")
                
        except Exception as e:
           new_ciff.is_valid = False

        return new_ciff
