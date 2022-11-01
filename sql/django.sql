--
-- PostgreSQL database dump
--

-- Dumped from database version 12.12 (Ubuntu 12.12-0ubuntu0.20.04.1)
-- Dumped by pg_dump version 12.12 (Ubuntu 12.12-0ubuntu0.20.04.1)

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
    phone_no character varying(16),
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
1	pbkdf2_sha256$150000$ukvwDFKKmtrS$9ribE7bWIRBU4v3fxt3hcoUqbOlFi/dVXnWDYufRiaQ=	2022-10-31 14:35:08.712882+05:30	t	admin			admin@gmail.com	t	t	2022-10-31 14:34:51.008891+05:30	\N	0	f	0	\N	0	https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png
2	pbkdf2_sha256$150000$TKhZSSRuuE8O$lp9kEtin1ooWR/F1PDtHbxWrwghcpaE1BycQBPvdONo=	2022-10-31 14:37:07.820244+05:30	f	adith	Alec	Mendez	tonequhop@mailinator.com	f	t	2022-10-31 14:37:01.671294+05:30	31	0	f	99998808	\N	0	https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png
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
1	contenttypes	0001_initial	2022-10-31 14:34:11.943104+05:30
2	contenttypes	0002_remove_content_type_name	2022-10-31 14:34:11.953753+05:30
3	auth	0001_initial	2022-10-31 14:34:12.001052+05:30
4	auth	0002_alter_permission_name_max_length	2022-10-31 14:34:12.041375+05:30
5	auth	0003_alter_user_email_max_length	2022-10-31 14:34:12.048374+05:30
6	auth	0004_alter_user_username_opts	2022-10-31 14:34:12.055554+05:30
7	auth	0005_alter_user_last_login_null	2022-10-31 14:34:12.066579+05:30
8	auth	0006_require_contenttypes_0002	2022-10-31 14:34:12.070091+05:30
9	auth	0007_alter_validators_add_error_messages	2022-10-31 14:34:12.077445+05:30
10	auth	0008_alter_user_username_max_length	2022-10-31 14:34:12.089229+05:30
11	auth	0009_alter_user_last_name_max_length	2022-10-31 14:34:12.097083+05:30
12	auth	0010_alter_group_name_max_length	2022-10-31 14:34:12.105686+05:30
13	auth	0011_update_proxy_permissions	2022-10-31 14:34:12.114261+05:30
14	authentication	0001_initial	2022-10-31 14:34:12.189553+05:30
15	admin	0001_initial	2022-10-31 14:34:12.243807+05:30
16	admin	0002_logentry_remove_auto_add	2022-10-31 14:34:12.271238+05:30
17	admin	0003_logentry_add_action_flag_choices	2022-10-31 14:34:12.281456+05:30
18	ecommerce	0001_initial	2022-10-31 14:34:12.349702+05:30
19	home	0001_initial	2022-10-31 14:34:12.372075+05:30
20	sessions	0001_initial	2022-10-31 14:34:12.389721+05:30
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: labouser
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
u9p63vio9rtaasf8adhklev3nxtpp2h6	NTFhNGE2MWJkM2FlZjhlMWYwZDM1MTdhZDcxMzQ5NzI3Yzc5ODFlYTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4YTZkODAzMGQyNTkxZGFhODQyODg2MzlhMDY4NWQ5MTQ3MGJmNDNiIn0=	2022-11-14 14:35:08.716637+05:30
7zzw072ullf99pc7qn3wb3yq5s89zj53	NDI3ZDRmYzVjNWVmNTZhNGJmMmQzNDRkNmU3YzgyNzk5YTY4NTNkZDp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwMGEzNzYxOWMyZGJkY2FkMDQ2OTc5OWQ3OGFhNmJiZDQ3NzQ0YmU5Iiwib3JkZXIiOjgyOTQ0LCJCdWlsZGluZyI6IkNvcnBvcmlzIGV0IHNlZCBkZXNlcnVudCBpbiB0ZSIsIlN0cmVldCI6IlN1bnQgbmlzaSBldCBpbiBtaW5pbWEgY29tbW9kbyIsIkxvY2FsaXR5IjoiRG8gbW9kaSBoaWMgbW9sZXN0aWFlIG1vbGxpdCBwIn0=	2022-11-14 14:40:20.849521+05:30
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
1	Logan Roberts	78	15	data:image/jpeg;base64,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
2	Samantha Bonner	5	22	https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR5HRx3wgJDbSv_9sa8ynlfWB9BeA5minB8Sg&usqp=CAU
3	Murphy Vinson	48	36	https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSB5HtGMAU8tNCbRGm0uTfzxftI-LRLunAC-Hl1pgqDg0C-d-A1OyCObZLnw5hHAZSxEDE&usqp=CAU
\.


--
-- Data for Name: ecommerce_productsmodel; Type: TABLE DATA; Schema: public; Owner: labouser
--

COPY public.ecommerce_productsmodel (id, "Product_name", "Price", "Quantity", "Image") FROM stdin;
2	Kareem Bates	114	692	data:image/jpeg;base64,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
1	Linus Williams	526	982	data:image/jpeg;base64,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
3	Quail Fischer	552	439	data:image/jpeg;base64,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
\.


--
-- Data for Name: ecommerce_purchasemodel; Type: TABLE DATA; Schema: public; Owner: labouser
--

COPY public.ecommerce_purchasemodel (id, phone, "Total", "Prices", "Quantity", "Product_name", username, first_name, last_name, email, street, building, locality, postal, status, order_id, date) FROM stdin;
1	67	1192	{114,526,552}	{1,1,1}	{"Kareem Bates","Linus Williams","Quail Fischer"}	adith	India	Mueller	kuxugavop@mailinator.com	Sunt nisi et in minima commodo	Corporis et sed deserunt in te	Do modi hic molestiae mollit p	523706	3	82944	2022-10-31
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

SELECT pg_catalog.setval('public.authentication_newusermodel_id_seq', 2, true);


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

SELECT pg_catalog.setval('public.django_migrations_id_seq', 20, true);


--
-- Name: ecommerce_cartmodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: labouser
--

SELECT pg_catalog.setval('public.ecommerce_cartmodel_id_seq', 3, true);


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

SELECT pg_catalog.setval('public.ecommerce_packagemodel_id_seq', 3, true);


--
-- Name: ecommerce_productsmodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: labouser
--

SELECT pg_catalog.setval('public.ecommerce_productsmodel_id_seq', 3, true);


--
-- Name: ecommerce_purchasemodel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: labouser
--

SELECT pg_catalog.setval('public.ecommerce_purchasemodel_id_seq', 1, true);


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

