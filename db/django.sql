--
-- PostgreSQL database dump
--

-- Dumped from database version 14.5 (Ubuntu 14.5-1.pgdg20.04+1)
-- Dumped by pg_dump version 14.5 (Ubuntu 14.5-1.pgdg20.04+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: labouser
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO labouser;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: labouser
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO labouser;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: labouser
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: labouser
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO labouser;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: labouser
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO labouser;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: labouser
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: labouser
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO labouser;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: labouser
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO labouser;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: labouser
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: authentication_jobmodel; Type: TABLE; Schema: public; Owner: labouser
--

CREATE TABLE public.authentication_jobmodel (
    id integer NOT NULL,
    job_title character varying(255) NOT NULL,
    category character varying(255) NOT NULL
);


ALTER TABLE public.authentication_jobmodel OWNER TO labouser;

--
-- Name: authentication_jobmodel_id_seq; Type: SEQUENCE; Schema: public; Owner: labouser
--

CREATE SEQUENCE public.authentication_jobmodel_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.authentication_jobmodel_id_seq OWNER TO labouser;

--
-- Name: authentication_jobmodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: labouser
--

ALTER SEQUENCE public.authentication_jobmodel_id_seq OWNED BY public.authentication_jobmodel.id;


--
-- Name: authentication_labourmodels; Type: TABLE; Schema: public; Owner: labouser
--

CREATE TABLE public.authentication_labourmodels (
    id integer NOT NULL,
    username character varying(25) NOT NULL,
    image_link character varying(10000) NOT NULL,
    job_title character varying(50) NOT NULL,
    rate double precision NOT NULL,
    work_type boolean NOT NULL,
    status integer NOT NULL
);


ALTER TABLE public.authentication_labourmodels OWNER TO labouser;

--
-- Name: authentication_labourmodels_id_seq; Type: SEQUENCE; Schema: public; Owner: labouser
--

CREATE SEQUENCE public.authentication_labourmodels_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.authentication_labourmodels_id_seq OWNER TO labouser;

--
-- Name: authentication_labourmodels_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: labouser
--

ALTER SEQUENCE public.authentication_labourmodels_id_seq OWNED BY public.authentication_labourmodels.id;


--
-- Name: authentication_newusermodel; Type: TABLE; Schema: public; Owner: labouser
--

CREATE TABLE public.authentication_newusermodel (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    phone_no bigint NOT NULL,
    rating integer NOT NULL,
    is_sub boolean NOT NULL,
    wallet double precision NOT NULL,
    subscribed_at date,
    package integer NOT NULL,
    image character varying(3000)
);


ALTER TABLE public.authentication_newusermodel OWNER TO labouser;

--
-- Name: authentication_newusermodel_groups; Type: TABLE; Schema: public; Owner: labouser
--

CREATE TABLE public.authentication_newusermodel_groups (
    id integer NOT NULL,
    newusermodel_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.authentication_newusermodel_groups OWNER TO labouser;

--
-- Name: authentication_newusermodel_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: labouser
--

CREATE SEQUENCE public.authentication_newusermodel_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.authentication_newusermodel_groups_id_seq OWNER TO labouser;

--
-- Name: authentication_newusermodel_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: labouser
--

ALTER SEQUENCE public.authentication_newusermodel_groups_id_seq OWNED BY public.authentication_newusermodel_groups.id;


--
-- Name: authentication_newusermodel_id_seq; Type: SEQUENCE; Schema: public; Owner: labouser
--

CREATE SEQUENCE public.authentication_newusermodel_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.authentication_newusermodel_id_seq OWNER TO labouser;

--
-- Name: authentication_newusermodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: labouser
--

ALTER SEQUENCE public.authentication_newusermodel_id_seq OWNED BY public.authentication_newusermodel.id;


--
-- Name: authentication_newusermodel_user_permissions; Type: TABLE; Schema: public; Owner: labouser
--

CREATE TABLE public.authentication_newusermodel_user_permissions (
    id integer NOT NULL,
    newusermodel_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.authentication_newusermodel_user_permissions OWNER TO labouser;

--
-- Name: authentication_newusermodel_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: labouser
--

CREATE SEQUENCE public.authentication_newusermodel_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.authentication_newusermodel_user_permissions_id_seq OWNER TO labouser;

--
-- Name: authentication_newusermodel_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: labouser
--

ALTER SEQUENCE public.authentication_newusermodel_user_permissions_id_seq OWNED BY public.authentication_newusermodel_user_permissions.id;


--
-- Name: authentication_requests; Type: TABLE; Schema: public; Owner: labouser
--

CREATE TABLE public.authentication_requests (
    id integer NOT NULL,
    username character varying(255) NOT NULL,
    worker_username character varying(255) NOT NULL,
    status boolean NOT NULL
);


ALTER TABLE public.authentication_requests OWNER TO labouser;

--
-- Name: authentication_requests_id_seq; Type: SEQUENCE; Schema: public; Owner: labouser
--

CREATE SEQUENCE public.authentication_requests_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.authentication_requests_id_seq OWNER TO labouser;

--
-- Name: authentication_requests_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: labouser
--

ALTER SEQUENCE public.authentication_requests_id_seq OWNED BY public.authentication_requests.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: labouser
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO labouser;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: labouser
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO labouser;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: labouser
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: labouser
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO labouser;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: labouser
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO labouser;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: labouser
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: labouser
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO labouser;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: labouser
--

CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO labouser;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: labouser
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: labouser
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO labouser;

--
-- Name: ecommerce_cartmodel; Type: TABLE; Schema: public; Owner: labouser
--

CREATE TABLE public.ecommerce_cartmodel (
    id integer NOT NULL,
    product_id integer NOT NULL,
    "Product_name" text NOT NULL,
    "Price" double precision NOT NULL,
    "Total" double precision NOT NULL,
    "Quantity" integer NOT NULL,
    "Image" text NOT NULL,
    username character varying(255) NOT NULL,
    cartnumber integer NOT NULL
);


ALTER TABLE public.ecommerce_cartmodel OWNER TO labouser;

--
-- Name: ecommerce_cartmodel_id_seq; Type: SEQUENCE; Schema: public; Owner: labouser
--

CREATE SEQUENCE public.ecommerce_cartmodel_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ecommerce_cartmodel_id_seq OWNER TO labouser;

--
-- Name: ecommerce_cartmodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: labouser
--

ALTER SEQUENCE public.ecommerce_cartmodel_id_seq OWNED BY public.ecommerce_cartmodel.id;


--
-- Name: ecommerce_checkoutmodel; Type: TABLE; Schema: public; Owner: labouser
--

CREATE TABLE public.ecommerce_checkoutmodel (
    id integer NOT NULL,
    product_id integer NOT NULL,
    "Products" text NOT NULL,
    "Total" double precision NOT NULL,
    "Quantity" integer NOT NULL,
    username character varying(255) NOT NULL
);


ALTER TABLE public.ecommerce_checkoutmodel OWNER TO labouser;

--
-- Name: ecommerce_checkoutmodel_id_seq; Type: SEQUENCE; Schema: public; Owner: labouser
--

CREATE SEQUENCE public.ecommerce_checkoutmodel_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ecommerce_checkoutmodel_id_seq OWNER TO labouser;

--
-- Name: ecommerce_checkoutmodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: labouser
--

ALTER SEQUENCE public.ecommerce_checkoutmodel_id_seq OWNED BY public.ecommerce_checkoutmodel.id;


--
-- Name: ecommerce_hiremodel; Type: TABLE; Schema: public; Owner: labouser
--

CREATE TABLE public.ecommerce_hiremodel (
    id integer NOT NULL,
    worker_name text NOT NULL,
    "Hire_name" text NOT NULL,
    "Name" text NOT NULL,
    "Place" text NOT NULL,
    "Work_mode" character varying(6) NOT NULL,
    "Phone" bigint NOT NULL,
    status integer NOT NULL,
    job_title character varying(20) NOT NULL,
    user_status boolean NOT NULL,
    worker_status boolean NOT NULL,
    rating integer NOT NULL
);


ALTER TABLE public.ecommerce_hiremodel OWNER TO labouser;

--
-- Name: ecommerce_hiremodel_id_seq; Type: SEQUENCE; Schema: public; Owner: labouser
--

CREATE SEQUENCE public.ecommerce_hiremodel_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ecommerce_hiremodel_id_seq OWNER TO labouser;

--
-- Name: ecommerce_hiremodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: labouser
--

ALTER SEQUENCE public.ecommerce_hiremodel_id_seq OWNED BY public.ecommerce_hiremodel.id;


--
-- Name: ecommerce_packagemodel; Type: TABLE; Schema: public; Owner: labouser
--

CREATE TABLE public.ecommerce_packagemodel (
    id integer NOT NULL,
    package_name character varying(50) NOT NULL,
    validity integer NOT NULL,
    cost double precision NOT NULL,
    image text NOT NULL
);


ALTER TABLE public.ecommerce_packagemodel OWNER TO labouser;

--
-- Name: ecommerce_packagemodel_id_seq; Type: SEQUENCE; Schema: public; Owner: labouser
--

CREATE SEQUENCE public.ecommerce_packagemodel_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ecommerce_packagemodel_id_seq OWNER TO labouser;

--
-- Name: ecommerce_packagemodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: labouser
--

ALTER SEQUENCE public.ecommerce_packagemodel_id_seq OWNED BY public.ecommerce_packagemodel.id;


--
-- Name: ecommerce_productsmodel; Type: TABLE; Schema: public; Owner: labouser
--

CREATE TABLE public.ecommerce_productsmodel (
    id integer NOT NULL,
    "Product_name" text NOT NULL,
    "Price" double precision NOT NULL,
    "Quantity" integer NOT NULL,
    "Image" text NOT NULL
);


ALTER TABLE public.ecommerce_productsmodel OWNER TO labouser;

--
-- Name: ecommerce_productsmodel_id_seq; Type: SEQUENCE; Schema: public; Owner: labouser
--

CREATE SEQUENCE public.ecommerce_productsmodel_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ecommerce_productsmodel_id_seq OWNER TO labouser;

--
-- Name: ecommerce_productsmodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: labouser
--

ALTER SEQUENCE public.ecommerce_productsmodel_id_seq OWNED BY public.ecommerce_productsmodel.id;


--
-- Name: ecommerce_purchasemodel; Type: TABLE; Schema: public; Owner: labouser
--

CREATE TABLE public.ecommerce_purchasemodel (
    id integer NOT NULL,
    phone bigint,
    "Total" double precision NOT NULL,
    "Prices" double precision[] NOT NULL,
    "Quantity" integer[] NOT NULL,
    "Product_name" character varying(100)[],
    username character varying(100) NOT NULL,
    first_name text NOT NULL,
    last_name text NOT NULL,
    email text NOT NULL,
    street text NOT NULL,
    building text NOT NULL,
    locality text NOT NULL,
    postal integer NOT NULL,
    status integer,
    order_id integer NOT NULL,
    date date NOT NULL
);


ALTER TABLE public.ecommerce_purchasemodel OWNER TO labouser;

--
-- Name: ecommerce_purchasemodel_id_seq; Type: SEQUENCE; Schema: public; Owner: labouser
--

CREATE SEQUENCE public.ecommerce_purchasemodel_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ecommerce_purchasemodel_id_seq OWNER TO labouser;

--
-- Name: ecommerce_purchasemodel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: labouser
--

ALTER SEQUENCE public.ecommerce_purchasemodel_id_seq OWNED BY public.ecommerce_purchasemodel.id;


--
-- Name: home_category; Type: TABLE; Schema: public; Owner: labouser
--

CREATE TABLE public.home_category (
    id integer NOT NULL,
    category_name character varying(255) NOT NULL
);


ALTER TABLE public.home_category OWNER TO labouser;

--
-- Name: home_category_id_seq; Type: SEQUENCE; Schema: public; Owner: labouser
--

CREATE SEQUENCE public.home_category_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.home_category_id_seq OWNER TO labouser;

--
-- Name: home_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: labouser
--

ALTER SEQUENCE public.home_category_id_seq OWNED BY public.home_category.id;


--
-- Name: home_transaction; Type: TABLE; Schema: public; Owner: labouser
--

CREATE TABLE public.home_transaction (
    id integer NOT NULL,
    username character varying(255) NOT NULL,
    product_name character varying(255) NOT NULL,
    total_price integer NOT NULL,
    date date NOT NULL,
    quantity integer NOT NULL,
    "Status" character varying(100) NOT NULL
);


ALTER TABLE public.home_transaction OWNER TO labouser;

--
-- Name: home_transaction_id_seq; Type: SEQUENCE; Schema: public; Owner: labouser
--

CREATE SEQUENCE public.home_transaction_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.home_transaction_id_seq OWNER TO labouser;

--
-- Name: home_transaction_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: labouser
--

ALTER SEQUENCE public.home_transaction_id_seq OWNED BY public.home_transaction.id;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: authentication_jobmodel id; Type: DEFAULT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.authentication_jobmodel ALTER COLUMN id SET DEFAULT nextval('public.authentication_jobmodel_id_seq'::regclass);


--
-- Name: authentication_labourmodels id; Type: DEFAULT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.authentication_labourmodels ALTER COLUMN id SET DEFAULT nextval('public.authentication_labourmodels_id_seq'::regclass);


--
-- Name: authentication_newusermodel id; Type: DEFAULT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.authentication_newusermodel ALTER COLUMN id SET DEFAULT nextval('public.authentication_newusermodel_id_seq'::regclass);


--
-- Name: authentication_newusermodel_groups id; Type: DEFAULT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.authentication_newusermodel_groups ALTER COLUMN id SET DEFAULT nextval('public.authentication_newusermodel_groups_id_seq'::regclass);


--
-- Name: authentication_newusermodel_user_permissions id; Type: DEFAULT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.authentication_newusermodel_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.authentication_newusermodel_user_permissions_id_seq'::regclass);


--
-- Name: authentication_requests id; Type: DEFAULT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.authentication_requests ALTER COLUMN id SET DEFAULT nextval('public.authentication_requests_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: ecommerce_cartmodel id; Type: DEFAULT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.ecommerce_cartmodel ALTER COLUMN id SET DEFAULT nextval('public.ecommerce_cartmodel_id_seq'::regclass);


--
-- Name: ecommerce_checkoutmodel id; Type: DEFAULT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.ecommerce_checkoutmodel ALTER COLUMN id SET DEFAULT nextval('public.ecommerce_checkoutmodel_id_seq'::regclass);


--
-- Name: ecommerce_hiremodel id; Type: DEFAULT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.ecommerce_hiremodel ALTER COLUMN id SET DEFAULT nextval('public.ecommerce_hiremodel_id_seq'::regclass);


--
-- Name: ecommerce_packagemodel id; Type: DEFAULT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.ecommerce_packagemodel ALTER COLUMN id SET DEFAULT nextval('public.ecommerce_packagemodel_id_seq'::regclass);


--
-- Name: ecommerce_productsmodel id; Type: DEFAULT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.ecommerce_productsmodel ALTER COLUMN id SET DEFAULT nextval('public.ecommerce_productsmodel_id_seq'::regclass);


--
-- Name: ecommerce_purchasemodel id; Type: DEFAULT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.ecommerce_purchasemodel ALTER COLUMN id SET DEFAULT nextval('public.ecommerce_purchasemodel_id_seq'::regclass);


--
-- Name: home_category id; Type: DEFAULT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.home_category ALTER COLUMN id SET DEFAULT nextval('public.home_category_id_seq'::regclass);


--
-- Name: home_transaction id; Type: DEFAULT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.home_transaction ALTER COLUMN id SET DEFAULT nextval('public.home_transaction_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: labouser
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: labouser
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: labouser
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add content type	4	add_contenttype
14	Can change content type	4	change_contenttype
15	Can delete content type	4	delete_contenttype
16	Can view content type	4	view_contenttype
17	Can add session	5	add_session
18	Can change session	5	change_session
19	Can delete session	5	delete_session
20	Can view session	5	view_session
21	Can add cart model	6	add_cartmodel
22	Can change cart model	6	change_cartmodel
23	Can delete cart model	6	delete_cartmodel
24	Can view cart model	6	view_cartmodel
25	Can add checkout model	7	add_checkoutmodel
26	Can change checkout model	7	change_checkoutmodel
27	Can delete checkout model	7	delete_checkoutmodel
28	Can view checkout model	7	view_checkoutmodel
29	Can add hire model	8	add_hiremodel
30	Can change hire model	8	change_hiremodel
31	Can delete hire model	8	delete_hiremodel
32	Can view hire model	8	view_hiremodel
33	Can add package model	9	add_packagemodel
34	Can change package model	9	change_packagemodel
35	Can delete package model	9	delete_packagemodel
36	Can view package model	9	view_packagemodel
37	Can add products model	10	add_productsmodel
38	Can change products model	10	change_productsmodel
39	Can delete products model	10	delete_productsmodel
40	Can view products model	10	view_productsmodel
41	Can add purchase model	11	add_purchasemodel
42	Can change purchase model	11	change_purchasemodel
43	Can delete purchase model	11	delete_purchasemodel
44	Can view purchase model	11	view_purchasemodel
45	Can add category	12	add_category
46	Can change category	12	change_category
47	Can delete category	12	delete_category
48	Can view category	12	view_category
49	Can add transaction	13	add_transaction
50	Can change transaction	13	change_transaction
51	Can delete transaction	13	delete_transaction
52	Can view transaction	13	view_transaction
53	Can add jobmodel	14	add_jobmodel
54	Can change jobmodel	14	change_jobmodel
55	Can delete jobmodel	14	delete_jobmodel
56	Can view jobmodel	14	view_jobmodel
57	Can add labourmodels	15	add_labourmodels
58	Can change labourmodels	15	change_labourmodels
59	Can delete labourmodels	15	delete_labourmodels
60	Can view labourmodels	15	view_labourmodels
61	Can add requests	16	add_requests
62	Can change requests	16	change_requests
63	Can delete requests	16	delete_requests
64	Can view requests	16	view_requests
65	Can add user	17	add_newusermodel
66	Can change user	17	change_newusermodel
67	Can delete user	17	delete_newusermodel
68	Can view user	17	view_newusermodel
\.


--
-- Data for Name: authentication_jobmodel; Type: TABLE DATA; Schema: public; Owner: labouser
--

COPY public.authentication_jobmodel (id, job_title, category) FROM stdin;
\.


--
-- Data for Name: authentication_labourmodels; Type: TABLE DATA; Schema: public; Owner: labouser
--

COPY public.authentication_labourmodels (id, username, image_link, job_title, rate, work_type, status) FROM stdin;
\.


--
-- Data for Name: authentication_newusermodel; Type: TABLE DATA; Schema: public; Owner: labouser
--

COPY public.authentication_newusermodel (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, phone_no, rating, is_sub, wallet, subscribed_at, package, image) FROM stdin;
3	pbkdf2_sha256$150000$PMkoMEAzJkFp$R8JYGdlojTtYblwcvhvQkE89WXjeZsIT0StmScGZVvA=	2022-10-31 15:07:28.298928+05:30	t	admin			admin@gmail.com	t	t	2022-10-31 15:06:30.380362+05:30	1234567890	0	f	0	\N	0	https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png
4	pbkdf2_sha256$150000$v2Dr2aP35T55$AFR1bMlG1J12iNxZeWrvmy/c16EeFUivy6t/oaF+zds=	2022-10-31 15:09:03.058473+05:30	f	rakesh	Eagan	Kelly	wugykypana@gmail.com	f	t	2022-10-31 15:08:49.98984+05:30	95	0	f	0	\N	0	https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png
5	pbkdf2_sha256$150000$HjtT0md8hY5V$TEAtYjQw0SBSvPn9hLJPcXoHtrCXjSUd1oIzIUP9lOQ=	2022-10-31 15:09:35.020088+05:30	f	akhil	Dorian	Ellison	laha@gmail.com	f	t	2022-10-31 15:09:21.532099+05:30	21	0	t	4000	\N	0	https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png
\.


--
-- Data for Name: authentication_newusermodel_groups; Type: TABLE DATA; Schema: public; Owner: labouser
--

COPY public.authentication_newusermodel_groups (id, newusermodel_id, group_id) FROM stdin;
\.


--
-- Data for Name: authentication_newusermodel_user_permissions; Type: TABLE DATA; Schema: public; Owner: labouser
--

COPY public.authentication_newusermodel_user_permissions (id, newusermodel_id, permission_id) FROM stdin;
\.


--
-- Data for Name: authentication_requests; Type: TABLE DATA; Schema: public; Owner: labouser
--

COPY public.authentication_requests (id, username, worker_username, status) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: labouser
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: labouser
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	contenttypes	contenttype
5	sessions	session
6	ecommerce	cartmodel
7	ecommerce	checkoutmodel
8	ecommerce	hiremodel
9	ecommerce	packagemodel
10	ecommerce	productsmodel
11	ecommerce	purchasemodel
12	home	category
13	home	transaction
14	authentication	jobmodel
15	authentication	labourmodels
16	authentication	requests
17	authentication	newusermodel
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: labouser
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2022-10-31 15:03:06.090073+05:30
2	contenttypes	0002_remove_content_type_name	2022-10-31 15:03:06.103+05:30
3	auth	0001_initial	2022-10-31 15:03:06.135655+05:30
4	auth	0002_alter_permission_name_max_length	2022-10-31 15:03:06.167568+05:30
5	auth	0003_alter_user_email_max_length	2022-10-31 15:03:06.176805+05:30
6	auth	0004_alter_user_username_opts	2022-10-31 15:03:06.18632+05:30
7	auth	0005_alter_user_last_login_null	2022-10-31 15:03:06.195618+05:30
8	auth	0006_require_contenttypes_0002	2022-10-31 15:03:06.198464+05:30
9	auth	0007_alter_validators_add_error_messages	2022-10-31 15:03:06.207112+05:30
10	auth	0008_alter_user_username_max_length	2022-10-31 15:03:06.213054+05:30
11	auth	0009_alter_user_last_name_max_length	2022-10-31 15:03:06.218012+05:30
12	auth	0010_alter_group_name_max_length	2022-10-31 15:03:06.223015+05:30
13	auth	0011_update_proxy_permissions	2022-10-31 15:03:06.227648+05:30
14	authentication	0001_initial	2022-10-31 15:03:06.262609+05:30
15	admin	0001_initial	2022-10-31 15:03:06.335568+05:30
16	admin	0002_logentry_remove_auto_add	2022-10-31 15:03:06.37161+05:30
17	admin	0003_logentry_add_action_flag_choices	2022-10-31 15:03:06.389185+05:30
18	ecommerce	0001_initial	2022-10-31 15:03:06.470833+05:30
19	home	0001_initial	2022-10-31 15:03:06.499965+05:30
20	sessions	0001_initial	2022-10-31 15:03:06.518031+05:30
21	authentication	0002_auto_20221031_0935	2022-10-31 15:06:09.76123+05:30
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: labouser
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
7o8ix401rcoyv5zt7b0kpy34y31kmi6c	NzhjMWE2YTU5MDZmYTQxMjg0NjcyZGYwNDFhNmY1OGI4MzE1MWY0NTp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2NzlkNjMyODA3NTdkMGE5NDlkY2Y4NWRkN2MwNWE5YTM2OTkyZDc1In0=	2022-11-14 15:07:28.300682+05:30
h8fpbqdrph7xmfor19zpaqpo302pk1kp	NTgyYmU1NzE0NTQwMGUzNmFiNzBhYTNjYTM4MTExZGEwM2NhZWFkYjp7Il9hdXRoX3VzZXJfaWQiOiI1IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1OTRiZGE3OTQyOTkzZTQxNjE1NGQxZmUyYmMyNTdmNWJjMWU0NjBjIn0=	2022-11-14 15:09:35.021864+05:30
\.


--
-- Data for Name: ecommerce_cartmodel; Type: TABLE DATA; Schema: public; Owner: labouser
--

COPY public.ecommerce_cartmodel (id, product_id, "Product_name", "Price", "Total", "Quantity", "Image", username, cartnumber) FROM stdin;
\.


--
-- Data for Name: ecommerce_checkoutmodel; Type: TABLE DATA; Schema: public; Owner: labouser
--

COPY public.ecommerce_checkoutmodel (id, product_id, "Products", "Total", "Quantity", username) FROM stdin;
\.


--
-- Data for Name: ecommerce_hiremodel; Type: TABLE DATA; Schema: public; Owner: labouser
--

COPY public.ecommerce_hiremodel (id, worker_name, "Hire_name", "Name", "Place", "Work_mode", "Phone", status, job_title, user_status, worker_status, rating) FROM stdin;
\.


--
-- Data for Name: ecommerce_packagemodel; Type: TABLE DATA; Schema: public; Owner: labouser
--

COPY public.ecommerce_packagemodel (id, package_name, validity, cost, image) FROM stdin;
1	Alisa Price	28	93	Sit molestiae corpo
\.


--
-- Data for Name: ecommerce_productsmodel; Type: TABLE DATA; Schema: public; Owner: labouser
--

COPY public.ecommerce_productsmodel (id, "Product_name", "Price", "Quantity", "Image") FROM stdin;
\.


--
-- Data for Name: ecommerce_purchasemodel; Type: TABLE DATA; Schema: public; Owner: labouser
--

COPY public.ecommerce_purchasemodel (id, phone, "Total", "Prices", "Quantity", "Product_name", username, first_name, last_name, email, street, building, locality, postal, status, order_id, date) FROM stdin;
\.


--
-- Data for Name: home_category; Type: TABLE DATA; Schema: public; Owner: labouser
--

COPY public.home_category (id, category_name) FROM stdin;
\.


--
-- Data for Name: home_transaction; Type: TABLE DATA; Schema: public; Owner: labouser
--

COPY public.home_transaction (id, username, product_name, total_price, date, quantity, "Status") FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: labouser
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: labouser
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: labouser
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 68, true);


--
-- Name: authentication_jobmodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: labouser
--

SELECT pg_catalog.setval('public.authentication_jobmodel_id_seq', 1, false);


--
-- Name: authentication_labourmodels_id_seq; Type: SEQUENCE SET; Schema: public; Owner: labouser
--

SELECT pg_catalog.setval('public.authentication_labourmodels_id_seq', 1, false);


--
-- Name: authentication_newusermodel_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: labouser
--

SELECT pg_catalog.setval('public.authentication_newusermodel_groups_id_seq', 1, false);


--
-- Name: authentication_newusermodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: labouser
--

SELECT pg_catalog.setval('public.authentication_newusermodel_id_seq', 5, true);


--
-- Name: authentication_newusermodel_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: labouser
--

SELECT pg_catalog.setval('public.authentication_newusermodel_user_permissions_id_seq', 1, false);


--
-- Name: authentication_requests_id_seq; Type: SEQUENCE SET; Schema: public; Owner: labouser
--

SELECT pg_catalog.setval('public.authentication_requests_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: labouser
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: labouser
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 17, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: labouser
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 21, true);


--
-- Name: ecommerce_cartmodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: labouser
--

SELECT pg_catalog.setval('public.ecommerce_cartmodel_id_seq', 1, false);


--
-- Name: ecommerce_checkoutmodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: labouser
--

SELECT pg_catalog.setval('public.ecommerce_checkoutmodel_id_seq', 1, false);


--
-- Name: ecommerce_hiremodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: labouser
--

SELECT pg_catalog.setval('public.ecommerce_hiremodel_id_seq', 1, false);


--
-- Name: ecommerce_packagemodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: labouser
--

SELECT pg_catalog.setval('public.ecommerce_packagemodel_id_seq', 1, true);


--
-- Name: ecommerce_productsmodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: labouser
--

SELECT pg_catalog.setval('public.ecommerce_productsmodel_id_seq', 1, false);


--
-- Name: ecommerce_purchasemodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: labouser
--

SELECT pg_catalog.setval('public.ecommerce_purchasemodel_id_seq', 1, false);


--
-- Name: home_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: labouser
--

SELECT pg_catalog.setval('public.home_category_id_seq', 1, false);


--
-- Name: home_transaction_id_seq; Type: SEQUENCE SET; Schema: public; Owner: labouser
--

SELECT pg_catalog.setval('public.home_transaction_id_seq', 1, false);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: authentication_jobmodel authentication_jobmodel_pkey; Type: CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.authentication_jobmodel
    ADD CONSTRAINT authentication_jobmodel_pkey PRIMARY KEY (id);


--
-- Name: authentication_labourmodels authentication_labourmodels_pkey; Type: CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.authentication_labourmodels
    ADD CONSTRAINT authentication_labourmodels_pkey PRIMARY KEY (id);


--
-- Name: authentication_newusermodel_groups authentication_newusermo_newusermodel_id_group_id_84496ce6_uniq; Type: CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.authentication_newusermodel_groups
    ADD CONSTRAINT authentication_newusermo_newusermodel_id_group_id_84496ce6_uniq UNIQUE (newusermodel_id, group_id);


--
-- Name: authentication_newusermodel_user_permissions authentication_newusermo_newusermodel_id_permissi_d69215ca_uniq; Type: CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.authentication_newusermodel_user_permissions
    ADD CONSTRAINT authentication_newusermo_newusermodel_id_permissi_d69215ca_uniq UNIQUE (newusermodel_id, permission_id);


--
-- Name: authentication_newusermodel_groups authentication_newusermodel_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.authentication_newusermodel_groups
    ADD CONSTRAINT authentication_newusermodel_groups_pkey PRIMARY KEY (id);


--
-- Name: authentication_newusermodel authentication_newusermodel_pkey; Type: CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.authentication_newusermodel
    ADD CONSTRAINT authentication_newusermodel_pkey PRIMARY KEY (id);


--
-- Name: authentication_newusermodel_user_permissions authentication_newusermodel_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.authentication_newusermodel_user_permissions
    ADD CONSTRAINT authentication_newusermodel_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: authentication_newusermodel authentication_newusermodel_username_key; Type: CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.authentication_newusermodel
    ADD CONSTRAINT authentication_newusermodel_username_key UNIQUE (username);


--
-- Name: authentication_requests authentication_requests_pkey; Type: CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.authentication_requests
    ADD CONSTRAINT authentication_requests_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: ecommerce_cartmodel ecommerce_cartmodel_pkey; Type: CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.ecommerce_cartmodel
    ADD CONSTRAINT ecommerce_cartmodel_pkey PRIMARY KEY (id);


--
-- Name: ecommerce_checkoutmodel ecommerce_checkoutmodel_pkey; Type: CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.ecommerce_checkoutmodel
    ADD CONSTRAINT ecommerce_checkoutmodel_pkey PRIMARY KEY (id);


--
-- Name: ecommerce_hiremodel ecommerce_hiremodel_pkey; Type: CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.ecommerce_hiremodel
    ADD CONSTRAINT ecommerce_hiremodel_pkey PRIMARY KEY (id);


--
-- Name: ecommerce_packagemodel ecommerce_packagemodel_pkey; Type: CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.ecommerce_packagemodel
    ADD CONSTRAINT ecommerce_packagemodel_pkey PRIMARY KEY (id);


--
-- Name: ecommerce_productsmodel ecommerce_productsmodel_pkey; Type: CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.ecommerce_productsmodel
    ADD CONSTRAINT ecommerce_productsmodel_pkey PRIMARY KEY (id);


--
-- Name: ecommerce_purchasemodel ecommerce_purchasemodel_pkey; Type: CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.ecommerce_purchasemodel
    ADD CONSTRAINT ecommerce_purchasemodel_pkey PRIMARY KEY (id);


--
-- Name: home_category home_category_pkey; Type: CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.home_category
    ADD CONSTRAINT home_category_pkey PRIMARY KEY (id);


--
-- Name: home_transaction home_transaction_pkey; Type: CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.home_transaction
    ADD CONSTRAINT home_transaction_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: labouser
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: labouser
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: labouser
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: labouser
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: authentication_newusermode_newusermodel_id_4c843c60; Type: INDEX; Schema: public; Owner: labouser
--

CREATE INDEX authentication_newusermode_newusermodel_id_4c843c60 ON public.authentication_newusermodel_user_permissions USING btree (newusermodel_id);


--
-- Name: authentication_newusermode_permission_id_fc606b82; Type: INDEX; Schema: public; Owner: labouser
--

CREATE INDEX authentication_newusermode_permission_id_fc606b82 ON public.authentication_newusermodel_user_permissions USING btree (permission_id);


--
-- Name: authentication_newusermodel_groups_group_id_c1da9373; Type: INDEX; Schema: public; Owner: labouser
--

CREATE INDEX authentication_newusermodel_groups_group_id_c1da9373 ON public.authentication_newusermodel_groups USING btree (group_id);


--
-- Name: authentication_newusermodel_groups_newusermodel_id_bd7e3661; Type: INDEX; Schema: public; Owner: labouser
--

CREATE INDEX authentication_newusermodel_groups_newusermodel_id_bd7e3661 ON public.authentication_newusermodel_groups USING btree (newusermodel_id);


--
-- Name: authentication_newusermodel_username_cf3bbbae_like; Type: INDEX; Schema: public; Owner: labouser
--

CREATE INDEX authentication_newusermodel_username_cf3bbbae_like ON public.authentication_newusermodel USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: labouser
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: labouser
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: labouser
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: labouser
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authentication_newusermodel_groups authentication_newus_group_id_c1da9373_fk_auth_grou; Type: FK CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.authentication_newusermodel_groups
    ADD CONSTRAINT authentication_newus_group_id_c1da9373_fk_auth_grou FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authentication_newusermodel_user_permissions authentication_newus_newusermodel_id_4c843c60_fk_authentic; Type: FK CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.authentication_newusermodel_user_permissions
    ADD CONSTRAINT authentication_newus_newusermodel_id_4c843c60_fk_authentic FOREIGN KEY (newusermodel_id) REFERENCES public.authentication_newusermodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authentication_newusermodel_groups authentication_newus_newusermodel_id_bd7e3661_fk_authentic; Type: FK CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.authentication_newusermodel_groups
    ADD CONSTRAINT authentication_newus_newusermodel_id_bd7e3661_fk_authentic FOREIGN KEY (newusermodel_id) REFERENCES public.authentication_newusermodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: authentication_newusermodel_user_permissions authentication_newus_permission_id_fc606b82_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.authentication_newusermodel_user_permissions
    ADD CONSTRAINT authentication_newus_permission_id_fc606b82_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_authentic; Type: FK CONSTRAINT; Schema: public; Owner: labouser
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_authentic FOREIGN KEY (user_id) REFERENCES public.authentication_newusermodel(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

